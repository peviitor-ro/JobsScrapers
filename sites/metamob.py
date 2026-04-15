#
#
#
# metamob > https://www.metamob.ro/ro/companie/cariera

from sites.website_scraper_bs4 import BS4Scraper
import requests
from bs4 import BeautifulSoup

class metamobScraper(BS4Scraper):
    
    """
    A class for scraping job data from metamob website.
    """
    url = 'https://www.metamob.ro/ro/companie/cariera'
    url_logo = 'https://www.metamob.ro/images/1000x200_logo_metamob.png'
    company_name = 'metamob'
    wayback_url = 'https://web.archive.org/web/20250116050655/https://www.metamob.ro/ro/companie/cariera'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self._set_headers()
        try:
            response = requests.get(self.url, headers=self.DEFAULT_HEADERS, verify=False, timeout=30)
            self.soup = BeautifulSoup(response.content, 'lxml')
        except requests.exceptions.RequestException:
            response = requests.get(self.wayback_url, headers=self.DEFAULT_HEADERS, verify=False, timeout=30)
            self.soup = BeautifulSoup(response.content, 'lxml')
    
    def scrape_jobs(self):
        """
        Scrape job data from metamob website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "caption")
        job_url_elements = self.get_jobs_elements('class_', 'itemReadmore')
        
        self.job_titles = self.get_jobs_details_tag('title', job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)

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
            if 'metamob.ro' in job_url:
                job_url = 'https://www.metamob.ro' + job_url.split('metamob.ro')[1]
            elif not job_url.startswith('http'):
                job_url = f"https://www.metamob.ro{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", "Satu Mare")

if __name__ == "__main__":
    metamob = metamobScraper()
    metamob.get_response()
    metamob.scrape_jobs()
    metamob.sent_to_future()
    
    
