#
#
#
# Nokia > https://careers.nokia.com/jobs/search/39325305/page1

from website_scraper_selenium import SeleniumScraper
from math import ceil

class NokiaScrapper(SeleniumScraper):
    
    """
    A class for scraping job data from Nokia website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the SeleniumScraper class.
        """
        self.URL = url
        super().__init__(company_name, company_logo_url)

    def setup_driver(self):
        self.driver()
        self.set_expected_wait()
        self.open_website(self.URL)
    
    def scrape_jobs(self):
        """
        Itterate over all the pages available and Scrape job data from Nokia website.
        """
        self.page_cap = ceil(int(self.get_page_cap('class_name', 'total_results')) / 10)
        
        for page in range(1, self.page_cap+1):
            new_url = self.URL[:-1]
            self.open_website(f'{new_url}{page}')
            self.job_titles = self.get_job_details('css_selector', 'p:nth-child(2) > a')
            self.job_urls = self.get_job_links('css_selector', 'p:nth-child(2) > a')
            
            self.format_data()
        
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """

        for job_title, job_url in zip(self.job_titles, self.job_urls):
            if job_url:
                self.create_jobs_dict(job_title, job_url, "Romania", "Romania")

if __name__ == "__main__":
    URL = 'https://careers.nokia.com/jobs/search/39325305/page1'
    URL_LOGO = 'https://careers.nokia.com/media/client_4_s2_r0_v1677590599579_main.png'
    company_name = 'Nokia'
    Nokia = NokiaScrapper(company_name, URL, URL_LOGO)
    Nokia.setup_driver()
    Nokia.scrape_jobs()
    