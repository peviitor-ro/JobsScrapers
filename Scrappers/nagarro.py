import requests
import uuid
from setup_api import UpdatePeviitorAPI
from update_logo import update_logo

class NagarroScrape:
    
    """
    A class for scraping job data from Nagarro website.
    """
    
    def __init__(self, company_name: str, url: str):
        """
        Defining de url, company name for the request and formatted data list for the jobs scrapped
        """
        self.company_name = company_name
        self.URL = url
        self.formated_data = []
    
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
        self.response = requests.get(
            self.URL,
            headers=self.headers).json()
    
    def get_job_titles(self):
        """
        Retrieves the job titles.
        """
        self.job_titles = [job_title['Job_Title'] for job_title in self.response["value"]]

    def get_job_city(self):
        """
        Retrieves the job cities.
        """
        self.job_cities = [job_city['Job_City'] for job_city in self.response["value"]]

    def get_job_country(self):
        """
        Retrieves the job countries.
        """
        self.job_countries = [job_country['Job_Country'] for job_country in self.response["value"]]

    def get_job_url(self):
        """
        Retrieves the job URLs.
        """
        self.job_urls = [job_url['Job_Url'] for job_url in self.response["value"]]

    def format_data(self):
        """
        Itterate over all job details and append them, modify job city if remote
        """
        for job_title, job_url, job_country, job_city in zip(self.job_titles, self.job_urls, self.job_countries, self.job_cities):
            if job_city == "WFA/Remote":
                job_city = job_country
            self.formated_data.append({
                "id": str(uuid.uuid4()),
                "job_title": job_title,
                "job_link":  job_url,
                "company": "Nagarro",
                "country": job_country,
                "city": job_city
                })
    
    def send_to_viitor(self):
        """
        Sending the scrapped jobs in the future :)
        """
        api_load = UpdatePeviitorAPI(self.company_name, self.formated_data)
        api_load()
        update_logo("Nagarro", "https://www.nagarro.com/hubfs/NagarroWebsiteRedesign-Aug2020/Assets/Images/Nagarro%20green%20logo%20with%20title_opt.svg")

if __name__ == "__main__":
    URL = 'https://hiringautomation.table.core.windows.net/CareerSiteDim?sv=2019-02-02&se=2099-10-13T20%3A47%3A00Z&sp=r&sig=%2FTWLo6vw7gzgOiS9b5wchECIjqFaaaIPV8Rs55P0W98%3D&tn=CareerSiteDim&$select=Expertise,Job_Title,Job_City,Job_Country,Level_name,Value,Job_Url,Is_job_remote_friendly,is_multiple_experience_required,RowKey&$filter=Job_Country%20eq%20%27Romania%27'
    company_name = 'Nagarro'
    Nagarro = NagarroScrape(company_name, URL)
    Nagarro.request_headers()
    Nagarro.get_response()
    Nagarro.get_job_titles()
    Nagarro.get_job_city()
    Nagarro.get_job_country()
    Nagarro.get_job_url()
    Nagarro.format_data()
    Nagarro.send_to_viitor()