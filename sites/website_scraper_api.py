from sites.setup_api import UpdatePeviitorAPI
from sites.update_logo import update_logo
from getCounty import get_county
import json


# Work in progress this might change significant during the creation of the following scrappers, might need further testing and improvements
class WebsiteScraperAPI:
    """
    A class for scraping job data from a website.
    """

    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Define the URL, company name for the request, and initialize the formatted data list for the scraped jobs.
        """
        self.company_name = company_name
        self.logo_url = company_logo_url
        self.URL = url
        self.formatted_data = []
        
    def get_jobs_response(self, response):
        """
        Retrieve the response.
        """
        self.jobs_response = response

    def post_jobs_response(self, response):
        """
        Send a GET request and retrieve the response.
        """
        self.jobs_response = response

    def get_job_details(self, job_detail_path):
        """
        Grab all the jobs detail needed for the json
        """
        job_details = []
        for job_data in self.jobs_response:
            result = job_data
            for path in job_detail_path:
                result = result[path]
            job_details.append(result)
            
        return job_details

    def get_county(self, city):
        return get_county(city)

    def create_jobs_dict(self, job_title, job_url, job_country, job_city, remote='On-site'):
        """
        Create the job dictionary for the future api
        """
        # Define a list for counties in case there is more than one
        self.counties = []
        
        # Get the county using the city
        if type(job_city) == list:
            for city in job_city:
                self.counties.append(self.get_county(city))
            job_county = self.counties
        else:
            job_county = self.get_county(job_city)
                
        self.formatted_data.append({
            "job_title": job_title,
            "job_link": job_url,
            "company": self.company_name,
            "country": job_country,
            "county": job_county,
            "city": job_city,
            "remote": remote
            
        })

    def send_to_viitor(self):
        """
        Sending the scrapped jobs to the future :)
        """
        api_load = UpdatePeviitorAPI(self.company_name, self.formatted_data)
        api_load()
        update_logo(self.company_name, self.logo_url)
        print(json.dumps(self.formatted_data, indent=4, sort_keys=True))
