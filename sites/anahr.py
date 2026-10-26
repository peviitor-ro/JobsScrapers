#
#
#
# anahr > https://www.anahr.ro/oportunitati-angajare

from sites.website_scraper_api import WebsiteScraperAPI
from bs4 import BeautifulSoup
import requests


class anahrScraper(WebsiteScraperAPI):
    
    """
    A class for scraping job data from anahr website.
    """
    url = 'https://www.anahr.ro/'
    url_jobs = 'https://www.anahr.ro/oportunitati-angajare'
    url_logo = 'https://anahr.ro/wp-content/uploads/2023/01/logo-01.svg'
    company_name = 'anahr'
    
    def __init__(self):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(self.company_name, self.url, self.url_logo)

    def set_headers(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def get_response(self):
        """
        Send a GET request and retrieve the jobs response.
        """
        self.set_headers()
        response = requests.get(self.url_jobs, headers=self.headers, timeout=600)
        soup = BeautifulSoup(response.content, 'lxml')
        self.job_details = self.parse_job_cards(soup)

        if not self.job_details:
            response = requests.get(self.url, headers=self.headers, timeout=600)
            soup = BeautifulSoup(response.content, 'lxml')
            self.job_details = self.parse_job_cards(soup)

        self.get_jobs_response(self.job_details)

    @staticmethod
    def clean_text(text):
        return ' '.join(text.replace('\xa0', ' ').split())

    def parse_job_cards(self, soup):
        """
        The current website is built with Wix. The open positions are rendered
        server side as repeater cards. Each card holds the job title, the
        location metadata and a link to the job detail page.
        """
        jobs = []
        seen_urls = set()

        for link in soup.select('a[href*="/jobs-2/"]'):
            job_url = link.get('href', '').strip()
            if not job_url or job_url in seen_urls:
                continue

            card = link.find_parent(class_='wixui-repeater__item')
            if card is None:
                card = link.find_parent(class_='wixui-repeater')
            if card is None:
                continue

            title_element = card.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            if title_element is None:
                continue

            job_title = self.clean_text(title_element.get_text(' ', strip=True))
            if not job_title:
                continue

            location = ''
            for paragraph in card.find_all('p'):
                text = self.clean_text(paragraph.get_text(' ', strip=True))
                if '·' in text and not text.lower().startswith('updated'):
                    location = text
                    break

            location_parts = [part.strip() for part in location.split('·') if part.strip()]
            remote = 'on-site'
            job_city = ''

            for part in location_parts:
                lowered = part.lower()
                if 'remote' in lowered or 'wfa' in lowered:
                    remote = 'remote'
                elif 'hybrid' in lowered:
                    remote = 'hybrid'
                elif not job_city and not any(
                    word in lowered
                    for word in ('contract', 'full-time', 'part-time', 'b2b', 'multi-year')
                ):
                    job_city = part.split('(')[0].split(',')[0].strip()

            if not job_city:
                job_city = 'Remote' if remote == 'remote' else 'România'

            jobs.append({
                'job_title': job_title,
                'job_url': job_url,
                'job_city': job_city,
                'remote': remote
            })
            seen_urls.add(job_url)

        return jobs

    def scrape_jobs(self):
        """
        Scrape job data from anahr website.
        """
        self.job_titles = self.get_job_details(['job_title'])
        self.job_cities = self.get_job_details(['job_city'])
        self.job_urls = self.get_job_details(['job_url'])
        self.job_remotes = self.get_job_details(['remote'])
        self.format_data()

    def sent_to_future(self):
        self.send_to_viitor()

    def return_data(self):
        self.set_headers()
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city, job_remote in zip(
            self.job_titles, self.job_urls, self.job_cities, self.job_remotes
        ):
            self.create_jobs_dict(job_title, job_url, "România", job_city, job_remote)


if __name__ == "__main__":
    anahr = anahrScraper()
    anahr.set_headers()
    anahr.get_response()
    anahr.scrape_jobs()
    anahr.sent_to_future()
