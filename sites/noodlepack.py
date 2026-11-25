#
# 
#
# noodlepack > https://noodlepack.ro/cariera-job-noodlepack/


import requests
from bs4 import BeautifulSoup

from sites.website_scraper_bs4 import BS4Scraper

class noodlepackScraper(BS4Scraper):
    
    """
    A class for scraping job data from noodlepack website.
    """
    url = 'https://noodlepack.ro/cariera-job-noodlepack/'
    wayback_url = 'https://web.archive.org/web/20260313114649id_/https://noodlepack.ro/cariera-job-noodlepack/'
    url_logo = 'https://noodlepack.ro/wp-content/themes/uny/img/logo.png'
    company_name = 'noodlepack'
    
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
            response = requests.get(self.wayback_url, headers=self.DEFAULT_HEADERS, verify=False, timeout=60)
            self.soup = BeautifulSoup(response.content, 'lxml')
    
    def scrape_jobs(self):
        """
        Scrape job data from noodlepack website.
        """

        job_title_elements = self.get_jobs_elements('css_', 'div.col-md-6.order2 > div > h3')
        job_urls_elements = self.get_jobs_elements('css_', 'div > div.col-md-6.order2 > div > div > a')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)
        
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
            job_url = "https://noodlepack.ro" + job_url
            self.create_jobs_dict(job_title, job_url, "România", ["Arad", "Brasov", "Baia Mare", "Bucuresti", "Cluj-Napoca", "Craiova", "Constanta", "Deva", "Iasi", "Oradea", "Pitesti", "Ploiesti", "Satu Mare", "Sibiu", "Suceava", "Timisoara"])

if __name__ == "__main__":
    noodlepack = noodlepackScraper()
    noodlepack.get_response()
    noodlepack.scrape_jobs()
    noodlepack.sent_to_future()
    
    