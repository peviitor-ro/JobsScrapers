#
#
#
# pimcopy > https://pimcopy.ro/cariere

import requests
from bs4 import BeautifulSoup

from sites.website_scraper_bs4 import BS4Scraper

class pimcopyScraper(BS4Scraper):
    
    """
    A class for scraping job data from pimcopy website.
    """
    url = 'https://pimcopy.ro/cariere'
    archive_url = 'https://web.archive.org/web/2026id_/https://pimcopy.ro/cariere'
    job_selector = 'div.cell-8.contact-detalis > h3'
    url_logo = 'https://pimcopy.ro/assets/images/logo.png'
    company_name = 'pimcopy'
    
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)
        
    def _load_jobs(self, url, timeout):
        self._set_headers()
        response = requests.get(
            url, headers=self.DEFAULT_HEADERS, verify=False, timeout=timeout
        )
        self.soup = BeautifulSoup(response.content, 'lxml')
        return self.get_jobs_elements('css_', self.job_selector)

    def get_response(self):
        self.soup = BeautifulSoup('', 'lxml')
        for url, timeout in ((self.url, 20), (self.archive_url, 45)):
            try:
                if self._load_jobs(url, timeout):
                    return
            except requests.RequestException:
                continue
    
    def scrape_jobs(self):
        """
        Scrape job data from pimcopy website.
        """

        job_elements = self.get_jobs_elements('css_', self.job_selector)
        
        self.job_titles = self.get_jobs_details_text(job_elements)

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
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")
            self.job_count += 1

if __name__ == "__main__":
    pimcopy = pimcopyScraper()
    pimcopy.get_response()
    pimcopy.scrape_jobs()
    pimcopy.sent_to_future()
    
    

