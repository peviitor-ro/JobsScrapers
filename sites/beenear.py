#
#
#
# Beenear > https://www.beenear.com/career/

from website_scraper_bs4 import BS4Scraper
from math import ceil

class BeenearScrapper(BS4Scraper):
    
    """
    A class for scraping job data from Beenear website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Beenear website.
        """
        job_titles_elements = self.get_jobs_elements('css_', 'div > h3 > a')
        job_urls_elements = self.get_jobs_elements('css_', "div > h3 > a")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)
        
            
        self.format_data()
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            if job_title and job_url:
                self.create_jobs_dict(job_title, job_url, "Romania", "Iasi")

if __name__ == "__main__":
    URL = 'https://www.beenear.com/career/'
    URL_LOGO = 'https://beenear.com/wp-content/uploads/2020/07/logo.svg'
    company_name = 'Beenear'
    Beenear = BeenearScrapper(company_name, URL, URL_LOGO)
    Beenear.get_response()
    Beenear.scrape_jobs()
    
    

