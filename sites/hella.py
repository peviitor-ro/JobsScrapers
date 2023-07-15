#
#
#
# hella > https://hella.csod.com/ux/ats/careersite/3/home?c=hella&country=ro&lang=en-US

import requests
from website_scraper_api import WebsiteScraperAPI
from sites.website_scraper_bs4 import BS4Scraper
from bs4 import BeautifulSoup
import re

class hellaScrape(WebsiteScraperAPI):
    
    """
    A class for scraping job data from hella website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(company_name, url, company_logo_url)
    
    def get_token(self):
        # Send a GET request to the webpage
        response = requests.get("https://hella.csod.com/ux/ats/careersite/3/home?c=hella&country=ro&lang=en-US")  # Replace with the actual URL of the webpage

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'lxml')

        # Extract the value of the "token" key
        token_match = re.search(r'"token":"([^"]+)"', str(soup))
        if token_match:
            self.token = f"Bearer {token_match.group(1)}"
        else:
            print("Token not found in the string.")
    
    def set_headers(self):
        self.headers = {
        'accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
        'authorization': self.token,
        }
    
    def set_json_data(self):
        self.json_data = {
            'careerSiteId': 3,
            'careerSitePageId': 3,
            'pageNumber': 1,
            'pageSize': 200,
            'cultureId': 1,
            'searchText': '',
            'cultureName': 'en-US',
            'states': [],
            'countryCodes': [
                'ro',
            ],
            'cities': [],
            'placeID': '',
            'radius': None,
            'postingsWithinDays': None,
            'customFieldCheckboxKeys': [],
            'customFieldDropdowns': [],
            'customFieldRadios': [],
        }
    
    def post_response(self):
        """
        Send a post request and retrieve the jobs response.
        """
        self.job_details = requests.post(self.URL, headers=self.headers, json=self.json_data).json()['data']['requisitions']
        self.get_jobs_response(self.job_details)

    def scrape_jobs(self):
        """
        Scrape job data from hella website.
        """
        # Get titles
        self.job_titles = self.get_job_details(['displayJobTitle'])
        
        # Get cities
        unformated_job_cities = self.get_job_details(['locations'])
        self.job_cities = [job_city[0]['city'] for job_city in unformated_job_cities]
        
        # Get url ids
        self.job_urls = self.get_job_details(['requisitionId'])
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
            job_url = f"https://hella.csod.com/ux/ats/careersite/3/home/requisition/{job_url}?c=hella&lang=en-US"
            self.create_jobs_dict(job_title, job_url, "Romania", job_city)
        

if __name__ == "__main__":
    URL = 'https://uk.api.csod.com/rec-job-search/external/jobs'
    URL_LOGO = 'https://www.hella.com/hella-ro/assets/images/layout_global/ForviaHella_Logo.svg'
    company_name = 'hella'
    hella = hellaScrape(company_name, URL, URL_LOGO)
    hella.get_token()
    hella.set_headers()
    hella.set_json_data()
    hella.post_response()
    hella.scrape_jobs()
    hella.send_to_viitor()