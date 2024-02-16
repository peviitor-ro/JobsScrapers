#
#
#
# Creatopy > https://creatopy.bamboohr.com/careers/

import requests
from sites.website_scraper_api import WebsiteScraperAPI

class CreatopyScraper(WebsiteScraperAPI):
    
    """
    A class for scraping job data from Creatopy website.
    """
    url = 'https://creatopy.bamboohr.com/careers/list'
    url_logo = 'https://images4.bamboohr.com/146133/logos/cropped.jpg?v=51'
    company_name = 'Creatopy'
    
    def __init__(self):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(self.company_name, self.url, self.url_logo)
    
    def set_headers(self):
        self.headers = {
            'Accept': 'application/json'
        }
    
    def get_response(self):
        """
        Send a GET request and retrieve the jobs response.
        """
        self.job_details = requests.get(self.URL, headers=self.headers).json()['result']
        self.get_jobs_response(self.job_details)


    def scrape_jobs(self):
        """
        Scrape job data from Creatopy website.
        """
        self.job_titles = self.get_job_details(['jobOpeningName'])
        self.job_cities = self.get_job_details(['location', 'city'])
        # self.job_countries = self.get_job_details(['location', 'state'])
        self.job_urls = self.get_job_details(['id'])
        self.job_type = self.get_job_details(['locationType'])
        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.set_headers()
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city, job_type in zip(self.job_titles, self.job_urls, self.job_cities, self.job_type):
            job_url = f"https://creatopy.bamboohr.com/careers/{job_url}"
            if job_city == None or job_city == "Remote":
                job_city = "Oradea"
            
            # Remote type
            if job_type == "1":
                remote = "remote"
            elif job_type == "2":
                remote = "hybrid"
            else:
                remote = "on-site"
                
            self.create_jobs_dict(job_title, job_url, "România", job_city, remote)
        

if __name__ == "__main__":
    Creatopy = CreatopyScraper()
    Creatopy.set_headers()
    Creatopy.get_response()
    Creatopy.scrape_jobs()
    Creatopy.sent_to_future()