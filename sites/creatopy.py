import requests
import uuid
from website_scrapper_api import WebsiteScraperAPI
from setup_api import UpdatePeviitorAPI
from update_logo import update_logo

class CreatopyScrape(WebsiteScraperAPI):
    
    """
    A class for scraping job data from Creatopy website.
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
        self.get_job_titles(['jobOpeningName'])
        self.get_job_city(['location', 'city'])
        self.get_job_country(['location', 'state'])
        self.get_job_url(['id'])
        self.format_data()
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_country, job_city in zip(self.job_titles, self.job_urls, self.job_countries, self.job_cities):
            job_url = f"https://creatopy.bamboohr.com/careers/{job_url}"
            if job_city == None or job_city == "Remote":
                job_city = "Romania"
            if job_country == None or job_country == "Remote":
                job_country = "Romania"
            if job_url:
                self.create_jobs_dict(job_title, job_url, job_country, job_city)
        

if __name__ == "__main__":
    URL = 'https://creatopy.bamboohr.com/careers/list'
    URL_LOGO = 'https://images4.bamboohr.com/146133/logos/cropped.jpg?v=51'
    company_name = 'Creatopy'
    Creatopy = CreatopyScrape(company_name, URL, URL_LOGO)
    Creatopy.set_headers()
    Creatopy.get_response()
    Creatopy.scrape_jobs()