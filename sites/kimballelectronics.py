#
#
#
# kimballelectronics > https://kei.wd1.myworkdayjobs.com/GlobalKimballCareers?locations=fbecff70217d10da6c755135d69d6c29

import requests
from sites.website_scraper_api import WebsiteScraperAPI

class kimballelectronicsScrape(WebsiteScraperAPI):
    
    """
    A class for scraping job data from kimballelectronics website.
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
                'locations': [
                    'fbecff70217d10da6c755135d69d6c29',
                ],
            },
            'limit': 20,
            'offset': 0,
            'searchText': '',
        }
    
    def get_response(self):
        """
        Send a GET request and retrieve the jobs response.
        """
        self.job_details = requests.post(self.URL, headers=self.headers, json=self.json_data).json()['jobPostings']
        self.get_jobs_response(self.job_details)

    def scrape_jobs(self):
        """
        Scrape job data from kimballelectronics website.
        """
        self.job_titles = self.get_job_details(['title'])
        self.job_urls = self.get_job_details(['externalPath'])
        self.format_data()
    
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            job_url = f"https://kei.wd1.myworkdayjobs.com/en-US/GlobalKimballCareers{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", "Timisoara")
        

if __name__ == "__main__":
    URL = 'https://kei.wd1.myworkdayjobs.com/wday/cxs/kei/GlobalKimballCareers/jobs'
    URL_LOGO = 'https://www.kimballelectronics.com/images/default-source/default-album/logo97f9e1ec-d733-4299-b1b1-6cf4691c0ecc.png?sfvrsn=45be445e_2'
    company_name = 'kimballelectronics'
    kimballelectronics = kimballelectronicsScrape(company_name, URL, URL_LOGO)
    kimballelectronics.set_headers()
    kimballelectronics.set_json_data()
    kimballelectronics.get_response()
    kimballelectronics.scrape_jobs()
    kimballelectronics.sent_to_future()