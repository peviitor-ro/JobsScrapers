#
#
#
# Orange > https://www.orange.ro/jobs/joburi-disponibile


import requests
from sites.website_scraper_api import WebsiteScraperAPI

class OrangeScraper(WebsiteScraperAPI):
    
    """
    A class for scraping job data from Orange website.
    """
    url = 'https://www.orange.ro/ux-admin/api/jobs/getJobs?&order=closing_date&direction=desc'
    url_logo = 'https://www.orange.ro/imagini/orange-logo-static.svg'
    company_name = 'Orange'
    
    def __init__(self):
        """
        Defining de url, company name for the request and formatted data list for the jobs scrapped
        """
        super().__init__(self.company_name, self.url, self.url_logo)
    
    def request_headers(self):
        """
        Set the request headers.
        """
        self.headers = {
            'Accept': 'application/json'
        }
    
    def get_response(self):
        """
        Send a GET request and retrieve the response.
        """
        self.job_details = requests.get(
            self.url,
            headers=self.headers, timeout=600).json()
        self.get_jobs_response(self.job_details)
    
    def scrape_jobs(self):
        """
        Scrape job data from Orange website.
        """
        self.job_titles = self.get_job_details(['title'])
        self.job_cities = [job_city[0]['name'] for job_city in self.get_job_details(['location'])]
        self.job_urls = self.get_job_details(['url'])
        
        self.format_data()

    def format_data(self):
        job_country = 'Romania'   
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, job_country, job_city)
            
    
    
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.request_headers()
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

if __name__ == "__main__":
    Orange = OrangeScraper()
    Orange.request_headers()
    Orange.get_response()
    Orange.scrape_jobs()
    Orange.send_to_viitor()
