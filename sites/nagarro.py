#
#
#
# Nagarro > https://www.nagarro.com/en/careers/romania


import requests
import uuid
from sites.website_scraper_api import WebsiteScraperAPI

class NagarroScraper(WebsiteScraperAPI):
    
    """
    A class for scraping job data from Nagarro website.
    """
    url = 'https://hiringautomation.table.core.windows.net/CareerSiteDim?sv=2019-02-02&se=2099-10-13T20%3A47%3A00Z&sp=r&sig=%2FTWLo6vw7gzgOiS9b5wchECIjqFaaaIPV8Rs55P0W98%3D&tn=CareerSiteDim&$select=Expertise,Job_Title,Job_City,Job_Country,Level_name,Value,Job_Url,Is_job_remote_friendly,is_multiple_experience_required,RowKey&$filter=Job_Country%20eq%20%27Romania%27'
    url_logo = 'https://www.nagarro.com/hubfs/NagarroWebsiteRedesign-Aug2020/Assets/Images/Nagarro%20green%20logo%20with%20title_opt.svg'
    company_name = 'Nagarro'
    
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
            headers=self.headers).json()["value"]
        self.get_jobs_response(self.job_details)
    
    def scrape_jobs(self):
        """
        Scrape job data from sephora website.
        """
        self.job_titles = self.get_job_details(['Job_Title'])
        self.job_cities = self.get_job_details(['Job_City'])
        self.job_countries = self.get_job_details(['Job_Country'])
        self.job_urls = self.get_job_details(['Job_Url'])
        
        self.format_data()

    def format_data(self):
        """
        Itterate over all job details and append them, modify job city if remote
        """     
        for job_title, job_url, job_country, job_city in zip(self.job_titles, self.job_urls, self.job_countries, self.job_cities):
            if job_city == "WFA/Remote":
                remote = "remote"
            else:
                remote = "On-site"
            self.create_jobs_dict(job_title, job_url, job_country, ['Bucuresti', 'Brasov', 'Cluj-Napoca', 'Timisoara'], remote)
    
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.request_headers()
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

if __name__ == "__main__":
    Nagarro = NagarroScraper()
    Nagarro.request_headers()
    Nagarro.get_response()
    Nagarro.scrape_jobs()
    Nagarro.send_to_viitor()
