#
#
#
# sephora > https://www.inside-sephora.com/en/romania/join-us

import requests
from website_scraper_api import WebsiteScraperAPI

class sephoraScrape(WebsiteScraperAPI):
    
    """
    A class for scraping job data from sephora website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(company_name, url, company_logo_url)
    
    def set_headers(self):
        self.headers = {
            'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://www.inside-sephora.com/en/romania/join-us',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
        }
        
    def set_params(self):
        self.params = {
            'page': '1',
            'lang': 'en',
            'pageSize': '100',
            'market': '22',
        }
        
    def get_response(self):
        """
        Send a GET request and retrieve the jobs response.
        """
        self.job_details = requests.get(self.URL, headers=self.headers, params=self.params).json()['offers']
        self.get_jobs_response(self.job_details)


    def scrape_jobs(self):
        """
        Scrape job data from sephora website.
        """
        self.job_titles = self.get_job_details(['label'])
        self.job_cities = self.get_job_details(['field_job_city'])
        # self.job_countries = self.get_job_details(['location', 'state'])
        self.job_urls = self.get_job_details(['field_job_id'])
        
        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = f"https://jobs.sephora.com/job-invite/{job_url}"
            self.create_jobs_dict(job_title, job_url, "Romania", job_city)
        

if __name__ == "__main__":
    URL = 'https://www.inside-sephora.com/api/proxy/sap/search'
    URL_LOGO = 'https://bucurestimall.ro/wp-content/uploads/2016/12/sephora_logo_1024x.png'
    company_name = 'sephora'
    sephora = sephoraScrape(company_name, URL, URL_LOGO)
    sephora.set_headers()
    sephora.set_params()
    sephora.get_response()
    sephora.scrape_jobs()
    sephora.send_to_viitor()
    