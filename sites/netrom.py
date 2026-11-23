#
#
#
#
## Netrom > https://www.netromsoftware.ro/cariere/

import time

import requests
from bs4 import BeautifulSoup

from sites.website_scraper_bs4 import BS4Scraper

class NetromScraper(BS4Scraper):
    
    """
    A class for scraping job data from Netrom website.
    """
    url = 'https://www.netromsoftware.ro/cariere/'
    url_logo = 'https://www.netromsoftware.ro/wp-content/uploads/2019/09/Logo-NetRom-Software-300dpi.png'
    company_name = 'Netrom'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self._set_headers()
                response = requests.get(self.url, headers=self.DEFAULT_HEADERS, verify=False, timeout=30)
                self.soup = BeautifulSoup(response.content, 'lxml')
                return True
            except requests.exceptions.RequestException:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    print(f"Warning: Could not connect to {self.url}")
                    self.soup = BeautifulSoup("", "lxml")
                    return False
        return False
    
    def scrape_jobs(self):
        """
        Scrape job data from Netrom website.
        """

        job_elements = self.get_jobs_elements('css_', 'td > a')
        job_cities_elements = self.get_jobs_elements('css_', 'tr > td.location')
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)

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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    Netrom = NetromScraper()
    Netrom.get_response()
    Netrom.scrape_jobs()
    Netrom.sent_to_future()
    
    

