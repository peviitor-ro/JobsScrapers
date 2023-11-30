#
#
#
# sephora > https://www.inside-sephora.com/en/romania/join-us

import requests
from sites.website_scraper_api import WebsiteScraperAPI

class sephoraScraper(WebsiteScraperAPI):
    
    """
    A class for scraping job data from sephora website.
    """
    url = 'https://www.inside-sephora.com/api/proxy/sap/search'
    url_logo = 'https://bucurestimall.ro/wp-content/uploads/2016/12/sephora_logo_1024x.png'
    company_name = 'sephora'
    
    def __init__(self):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(self.company_name, self.url, self.url_logo)
    
    def set_headers(self):
        self.headers = {
            'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://www.inside-sephora.com/en/romania/join-us?market=22',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
        }
        
    def set_params(self):
        self.params = {
            'page': '1',
            'lang': 'en',
            'pageSize': '100',
            'origin': '22',
            'keywords': '',
            'function': '',
            'contract': '',
            'type': '',
            'location': '',
            'market': '22',
            'region': '',
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
        self.set_headers()
        self.set_params()
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = f"https://jobs.sephora.com/job-invite/{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", job_city.lower().title().replace("Cluj-napoca", "Cluj-Napoca"))
        

if __name__ == "__main__":
    sephora = sephoraScraper()
    sephora.set_headers()
    sephora.set_params()
    sephora.get_response()
    sephora.scrape_jobs()
    sephora.sent_to_future()
    