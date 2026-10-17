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
        response = requests.get(self.url, headers=self.headers, timeout=600)
        soup = BeautifulSoup(response.content, 'lxml')
        self.job_details = self.parse_job_cards(soup)
        self.get_jobs_response(self.job_details)

    def parse_job_cards(self, soup):
        """
        The current website is built with Wix. The open positions are rendered
        server side in the "Job-uri recente" section of the homepage as static
        cards. Each card holds the job title and the location in a pair of
        ``h2.font_2`` elements. The old Zoho Recruit portal no longer exists.
        """
        heading = soup.find(string=lambda text: text and 'Job-uri recente' in text)
        if heading is None:
            return []

        section = heading
        for _ in range(6):
            section = section.parent
            if section is None:
                return []
            if section.find('h2', class_='font_2') and 'Vezi detalii' in section.get_text():
                break

        jobs = []
        titles = [title.get_text(' ', strip=True) for title in section.find_all('h2', class_='font_2')]
        for index in range(0, len(titles) - 1, 2):
            job_title = titles[index]
            location = titles[index + 1]
            job_city = location.split(',')[0].strip()
            jobs.append({
                'job_title': job_title,
                'job_url': self.url_jobs,
                'job_city': job_city
            })

        return jobs

    def scrape_jobs(self):
        """
        Scrape job data from anahr website.
        """
        self.job_titles = self.get_job_details(['job_title'])
        self.job_cities = self.get_job_details(['job_city'])
        self.job_urls = self.get_job_details(['job_url'])
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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)


if __name__ == "__main__":
    anahr = anahrScraper()
    anahr.set_headers()
    anahr.get_response()
    anahr.scrape_jobs()
    anahr.sent_to_future()
