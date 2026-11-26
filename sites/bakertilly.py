#
#
#
# bakertilly > https://www.bakertilly.ro/careers/job-openings/

import ast
import math
import re
import urllib.parse

import requests
from bs4 import BeautifulSoup

from sites.website_scraper_bs4 import BS4Scraper

class bakertillyScraper(BS4Scraper):
    
    """
    A class for scraping job data from bakertilly website.
    """
    url = 'https://www.bakertilly.ro/careers/job-openings/'
    url_logo = 'https://www.bakertilly.ro/wp-content/uploads/2019/08/BK-Logoweb.jpg'
    company_name = 'bakertilly'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        })
        response = session.get(self.url, verify=False, timeout=600)
        if 'wsidchk' not in response.text:
            self.soup = BeautifulSoup(response.content, 'lxml')
            return

        page = response.text
        items = self._decode_challenge(page)
        a0w = {key: int(value, 16) for key, value in re.findall(
            r'(\w+):(0x[0-9a-f]+)', re.search(r'var a0W=\{(.*?)\}', page).group(1))}
        total = self._challenge_number(re.search(r',T=(.*?),f=window\[', page).group(1))
        total += self._challenge_number(re.search(r",e=(.*?),x='wsidchk'", page).group(1))
        timestamp = re.search(r",V\[c\(a0W\.\w+\)\]='(\d+)'", page)
        if timestamp is None:
            timestamp = re.search(r"\('ts','(\d+)'\)", page)
        form_id = re.search(r",Q\['value'\]=(.*?),Q\[", page)
        if form_id is None:
            form_id = re.search(r"\('id',(.*?)\)", page)
        endpoint = re.search(r",v='(/[^']+)'", page).group(1)
        pdata = re.search(r",N='([^']+)'", page).group(1)
        params = {
            'wsidchk': str(total),
            'pdata': pdata,
            'id': self._challenge_string(form_id.group(1), items, a0w),
            'ts': timestamp.group(1),
            'cttl': '0',
        }
        solve_url = urllib.parse.urljoin(self.url, endpoint) + '?' + urllib.parse.urlencode(params)
        response = session.get(solve_url, verify=False, timeout=600, headers={'Referer': self.url})
        self.soup = BeautifulSoup(response.content, 'lxml')

    @staticmethod
    def _decode_challenge(page):
        items = ast.literal_eval('[' + re.search(
            r'function a0f\(\)\{var J=\[(.*?)\]', page).group(1) + ']')
        keys = {key: int(value, 16) for key, value in re.findall(
            r'(\w+):(0x[0-9a-f]+)', re.search(r'var a0h=\{(.*?)\}', page).group(1))}
        target = int(re.search(r'\}\(a0f,(0x[0-9a-f]+)\)', page).group(1), 16)
        for _ in range(len(items) + 1):
            if bakertillyScraper._challenge_checksum(items, keys) == target:
                return items
            items.append(items.pop(0))
        raise ValueError('Could not decode challenge')

    @staticmethod
    def _challenge_checksum(items, keys):
        def value(index):
            match = re.match(r'^\s*([+-]?\d+)', items[index - 0x8f])
            return int(match.group(1)) if match else math.nan
        try:
            return (value(0xc0) * (-value(keys['C']) / 2)
                    - value(keys['T']) / 3
                    + value(keys['f']) / 4
                    - value(keys['d']) / 5 * (-value(keys['F']) / 6)
                    - value(0xb0) / 7
                    - value(0xc1) / 8
                    + value(keys['Q']) / 9 * (value(keys['V']) / 10))
        except (TypeError, ValueError, ZeroDivisionError):
            return math.nan

    @staticmethod
    def _challenge_string(expression, items, a0w):
        parts = []
        for code, literal in re.findall(r"c\((0x[0-9a-f]+|a0W\.\w+)\)|'([^']*)'", expression):
            if literal:
                parts.append(literal)
            else:
                index = int(code, 16) if code.startswith('0x') else a0w[code[4:]]
                parts.append(items[index - 0x8f])
        return ''.join(parts)

    @staticmethod
    def _challenge_number(expression):
        tokens = []
        pattern = re.compile(r"\+!\+\[\]|\+!\[\]|!!\[\]|\[\]|[()]|\+")
        position = 0
        while position < len(expression):
            if expression[position].isspace():
                position += 1
                continue
            match = pattern.match(expression, position)
            if match is None:
                raise ValueError('Unexpected challenge expression')
            tokens.append(match.group())
            position = match.end()
        state = {'index': 0}

        def primitive(value):
            return '' if isinstance(value, list) else value

        def number(value):
            value = primitive(value)
            return int(value) if value else 0

        def text(value):
            value = primitive(value)
            if value is True:
                return 'true'
            if value is False:
                return 'false'
            return str(value)

        def add(left, right):
            left, right = primitive(left), primitive(right)
            if isinstance(left, str) or isinstance(right, str):
                return text(left) + text(right)
            return left + right

        def parse_primary():
            token = tokens[state['index']]
            state['index'] += 1
            if token == '+':
                return number(parse_primary())
            if token == '(':
                value = parse_add()
                state['index'] += 1
                return value
            return {'+!+[]': 1, '+![]': 0, '!![]': True, '[]': []}[token]

        def parse_add():
            value = parse_primary()
            while state['index'] < len(tokens) and tokens[state['index']] == '+':
                state['index'] += 1
                value = add(value, parse_primary())
            return value

        return number(parse_add())
    
    def scrape_jobs(self):
        """
        Scrape job data from bakertilly website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "div.vc_gitem-zone.vc_gitem-zone-c > div > div > div > div > h4 > a")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_titles_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Bucuresti")
            # if "Bucharest" in job_title:
            #     self.create_jobs_dict(job_title, job_url, "România", "Bucuresti")
            # # If there is not () in the title it means its from the default location: Bucharest otherwise is from another country
            # if "(" not in job_title and ")" not in job_title:
            #     self.create_jobs_dict(job_title, job_url, "România", "Bucuresti")

if __name__ == "__main__":
    bakertilly = bakertillyScraper()
    bakertilly.get_response()
    bakertilly.scrape_jobs()
    bakertilly.sent_to_future()
    
    

