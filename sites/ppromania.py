#
#
#
# ppromania > https://ppromania.ro/en/career-opportunities/

from sites.website_scraper_bs4 import BS4Scraper
import subprocess
import re
import json
import os

try:
    import cloudscraper
    CLOUDSCRAPER_AVAILABLE = True
except ImportError:
    CLOUDSCRAPER_AVAILABLE = False


class ppromaniaScraper(BS4Scraper):

    """
    A class for scraping job data from ppromania website.
    """
    url = 'https://ppromania.ro/jm-ajax/get_listings/'
    url_logo = 'https://ppromania.ro/wp-content/uploads/2021/04/pp-Logo-web.png'
    company_name = 'ppromania'

    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)

    def scrape_jobs(self):
        """
        Scrape job data from ppromania website.
        """
        data = self._fetch_jobs_api()

        if not data or "html" not in data:
            print("WARNING: Could not fetch job data - site may be protected by bot detection")
            self.job_titles = []
            self.job_urls = []
            self.job_cities = []
            return

        self.job_titles = re.findall(r'<h3>(.*?)<\/h3>', data["html"])
        self.job_urls = re.findall(r'<a href="(.*?)">\n', data["html"])
        self.job_cities = re.findall(r'class="location">\n\t\t\t(.*?)\t\t</div>', data["html"])

        self.format_data()

    def _fetch_jobs_api(self):
        """
        Fetch jobs from the API endpoint.
        """
        if CLOUDSCRAPER_AVAILABLE:
            return self._fetch_with_cloudscraper()
        else:
            return self._fetch_with_curl()

    def _fetch_with_cloudscraper(self):
        """
        Fetch job data using cloudscraper to bypass bot protection.
        """
        scraper = cloudscraper.create_scraper(
            browser={'browser': 'chrome', 'platform': 'windows', 'desktop': True}
        )

        scraper.get('https://ppromania.ro/', timeout=30)

        response = scraper.post(self.url, timeout=30)

        if response.status_code == 200:
            try:
                data = response.json()
                if 'message' in data and 'bot-protection' in data.get('message', '').lower():
                    print(f"WARNING: {data['message']}")
                return data
            except json.JSONDecodeError:
                pass

        if 'Imunify360' in response.text or 'bot-protection' in response.text:
            print(f"WARNING: Bot protection blocked - IP needs to be whitelisted")

        return {"html": ""}

    def _fetch_with_curl(self):
        """
        Fetch job data using curl command with proper headers.
        """
        headers = [
            '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            '-H', 'Accept: application/json, text/javascript, */*; q=0.01',
            '-H', 'Accept-Language: en-US,en;q=0.5',
            '-H', 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
            '-H', 'X-Requested-With: XMLHttpRequest',
            '-H', 'Origin: https://ppromania.ro',
            '-H', 'Referer: https://ppromania.ro/',
        ]

        cmd = ['curl', '-s', '--http1.1'] + headers + ['-X', 'POST', '--data-raw', '', self.url]

        try:
            output = subprocess.check_output(cmd, timeout=30)
            output = output.decode("utf-8")

            try:
                data = json.loads(output)
                if 'message' in data and 'bot-protection' in data.get('message', '').lower():
                    print(f"WARNING: {data['message']}")
                return data
            except json.JSONDecodeError:
                pass

            if 'Imunify360' in output or 'bot-protection' in output:
                print(f"WARNING: Bot protection blocked - IP needs to be whitelisted")

        except subprocess.CalledProcessError as e:
            print(f"ERROR: curl failed with {e.returncode}")

        except subprocess.TimeoutExpired:
            print("ERROR: curl timed out")

        return {"html": ""}
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            if "Remote" in job_city:
                job_city = "all"
                remote = "remote"
            else:
                remote = "On-site"
                
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace(" / Ilfov", "").split(), remote)

if __name__ == "__main__":
    ppromania = ppromaniaScraper()
    ppromania.scrape_jobs()
    ppromania.sent_to_future()
    
    

