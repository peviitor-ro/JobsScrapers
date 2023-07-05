#
#
#
#
## Netfrom > https://www.netromsoftware.ro/jobs

from website_scraper_bs4 import BS4Scraper
from math import ceil

class NetromScrapper(BS4Scraper):
    
    """
    A class for scraping job data from Netrom website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(company_name, url, company_logo_url)
        
    def get_response(self):
        self.get_content()
    
    def scrape_jobs(self):
        """
        Scrape job data from Netrom website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div.left-column.simple-page > div > ul > li > a')
        job_urls_elements = self.get_jobs_elements('css_', "div.left-column.simple-page > div > ul > li > a")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements[1:])
        self.job_urls = self.get_jobs_details_href(job_urls_elements[1:])

        self.format_data()
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            if job_title and job_url:
                self.create_jobs_dict(job_title, job_url, "Romania", "Craiova")

if __name__ == "__main__":
    URL = 'https://www.netromsoftware.ro/jobs'
    URL_LOGO = 'https://www.netromsoftware.ro/images/logo.png'
    company_name = 'Netrom'
    Netrom = NetromScrapper(company_name, URL, URL_LOGO)
    Netrom.get_response()
    Netrom.scrape_jobs()
    
    

