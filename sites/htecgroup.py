#
#
#
# htecgroup > https://htecgroup.com/careers/

import requests
from website_scraper_api import WebsiteScraperAPI

class htecgroupScrape(WebsiteScraperAPI):
    
    """
    A class for scraping job data from htecgroup website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(company_name, url, company_logo_url)
    
    def set_params(self):
        self.params = {
            'stages': 'true',
            'language': 'en',
            'sort': 'modified_date',
            'page': '1',
            'perPage': '7',
            'status': 'Published',
            'd': '17839',
        }
    
    def get_response(self):
        """
        Send a GET request and retrieve the jobs response.
        """
        self.job_details = requests.get(self.URL, params=self.params).json()['Results']
        self.get_jobs_response(self.job_details)


    def scrape_jobs(self):
        """
        Scrape job data from htecgroup website.
        """
        self.job_titles = self.get_job_details(['Title'])
        # self.job_cities = self.get_job_details(['location', 'city'])
        # self.job_countries = self.get_job_details(['location', 'state'])
        self.job_urls = self.get_job_details(['AbsoluteUrl'])
        self.format_data()
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "Romania", "Romania")
        

if __name__ == "__main__":
    URL = 'https://api.talentlyft.com/public/jswidget/54388e55-d1d7-4bc1-ab98-41a2c4e7aea4/jobs'
    URL_LOGO = 'https://htecgroup.com/wp-content/uploads/2023/05/vectorhtec-logo.svg'
    company_name = 'htecgroup'
    htecgroup = htecgroupScrape(company_name, URL, URL_LOGO)
    htecgroup.set_params()
    htecgroup.get_response()
    htecgroup.scrape_jobs()