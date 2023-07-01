#
#
#
# CGM > https://cgm.wd3.myworkdayjobs.com/cgm?q=iasi&locationCountry=f2e609fe92974a55a05fc1cdc2852122

import requests
from website_scraper_api import WebsiteScraperAPI

class CGMScrape(WebsiteScraperAPI):
    
    """
    A class for scraping job data from CGM website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(company_name, url, company_logo_url)
    
    def set_headers(self):
        self.headers = {
            'Accept': 'application/json'
        }
    
    def set_json_data(self):
        self.json_data = {
        'appliedFacets': {
            'locationCountry': [
                'f2e609fe92974a55a05fc1cdc2852122',
            ],
        },
        'limit': 20,
        'offset': 0,
        'searchText': 'iasi',
        }
    
    def get_response(self):
        """
        Send a POST request and retrieve the jobs response.
        """
        self.job_details = requests.post(self.URL, headers=self.headers, json=self.json_data).json()['jobPostings']
        self.post_jobs_response(self.job_details)

    def scrape_jobs(self):
        """
        Scrape job data from CGM website.
        """
        self.job_titles = self.get_job_details(['title'])
        self.job_cities = self.get_job_details(['locationsText'])
        self.job_urls = self.get_job_details(['externalPath'])
        self.format_data()
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = f"https://cgm.wd3.myworkdayjobs.com/en-US/cgm{job_url}"
            if job_url and job_title and job_city:
                self.create_jobs_dict(job_title, job_url, "Romania", job_city)
        

if __name__ == "__main__":
    URL = 'https://cgm.wd3.myworkdayjobs.com/wday/cxs/cgm/cgm/jobs'
    URL_LOGO = 'https://www.cgm.com/_Resources/Static/Packages/Cgm.CgmCom/Assets/Icons/Logo/cgm-logo-large-376.png?bust=bf948c66'
    company_name = 'CGM'
    CGM = CGMScrape(company_name, URL, URL_LOGO)
    CGM.set_headers()
    CGM.set_json_data()
    CGM.get_response()
    CGM.scrape_jobs()