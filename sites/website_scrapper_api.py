import requests
import uuid
from setup_api import UpdatePeviitorAPI
from update_logo import update_logo


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

    # def set_request_headers(self, headers):
    #     """
    #     Set the request headers.
    #     """
    #     self.headers = headers

    def get_jobs_response(self, response):
        """
        Send a GET request and retrieve the response.
        """
        self.jobs_response = response

    def post_jobs_response(self, response):
        """
        Send a GET request and retrieve the response.
        """
        self.jobs_response = response


    def get_job_titles(self, job_title_path):
        """
        Retrieves the job titles from the response.
        """
        # self.job_titles = [job[job_title_path] for job in response]
        self.job_titles = []
        for job_data in self.jobs_response:
            result = job_data
            for path in job_title_path:
                result = result[path]
            self.job_titles.append(result)
        
        # print(self.job_titles)


    def get_job_city(self, job_cities_path):
        """
        Retrieves the job cities from the response.
        """
        # self.job_cities = [job[job_cities_path] for job in response]
        self.job_cities = []
        for job_data in self.jobs_response:
            result = job_data
            for path in job_cities_path:
                result = result[path]
            self.job_cities.append(result)

        # print(self.job_cities)

    def get_job_country(self, job_country_path):
        """
        Retrieves the job countries from the response.
        """
        # self.job_countries = [job[job_country_path] for job in response]
        self.job_countries = []
        for job_data in self.jobs_response:
            result = job_data
            for path in job_country_path:
                result = result[path]
            self.job_countries.append(result)

        # print(self.job_countries)


    def get_job_url(self, job_url_path):
        """
        Retrieves the job URLs from the response.
        """
        # self.job_urls = [job[job_url_path] for job in response]
        self.job_urls = []
        for job_data in self.jobs_response:
            result = job_data
            for path in job_url_path:
                result = result[path]
            self.job_urls.append(result)

        # print(self.job_urls)

    def create_jobs_dict(self, job_title, job_url, job_country, job_city):
        """
        Create the job dictionary for the future api
        """
        if job_url:
            self.formatted_data.append({
                "id": str(uuid.uuid4()),
                "job_title": job_title,
                "job_link": job_url,
                "company": self.company_name,
                "country": job_country,
                "city": job_city
            })
            

    def send_to_viitor(self):
        """
        Sending the scrapped jobs to the future :)
        """
        api_load = UpdatePeviitorAPI(self.company_name, self.formated_data)
        api_load()
        update_logo(self.company_name, self.logo_url)
