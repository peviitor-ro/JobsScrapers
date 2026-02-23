import requests
from bs4 import BeautifulSoup
from sites.setup_api import UpdatePeviitorAPI
from sites.update_logo import update_logo
from sites.getCounty import get_county
import json


class BS4Scraper:
    """
    A class for scraping job data from a website using BeautifulSoup (bs4).
    """

    def __init__(self, company_name: str, company_logo_url: str):
        """
        Define the URL, company name for the request, and initialize the formatted data list for the scraped jobs.
        """
        self.company_name = company_name
        self.logo_url = company_logo_url
        # self.URL = url
        self.formatted_data = []
    
    def _set_headers(self):
        self.DEFAULT_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_8_8; like Mac OS X) AppleWebKit/535.14 (KHTML, like Gecko) Chrome/49.0.3028.253 Mobile Safari/603.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Refer': 'https://google.com',
        'DNT': '1'
        }

    def get_content(self, url):
        self._set_headers()
        # Ignoring ssl cert check as many websites don't update it
        response = requests.get(url, headers=self.DEFAULT_HEADERS, verify=False, timeout=600)
        # response = requests.get(url, headers=self.DEFAULT_HEADERS)
        self.soup = BeautifulSoup(response.content, 'lxml')


    def get_jobs_elements(self, element_locator, element):
        """
        Grab all the elements from the page that match the locator and the element
        """
        if element_locator == "class_":
            job_details = self.soup.find_all(class_=element)
        elif element_locator == "id_":
            job_details = self.soup.find_all(id=element)
        elif element_locator == "name_":
            job_details = self.soup.find_all(name=element)
        elif element_locator == "css_":
            job_details = self.soup.select(element)
        else:
            raise ValueError("Invalid element locator type")
        
        return job_details
    
    def get_jobs_details_text(self, job_details):
        return [' '.join(job_detail.text.split()) for job_detail in job_details]

    def get_jobs_details_href(self, job_details):
        return [' '.join(job_detail.get('href').split()) for job_detail in job_details]

    def get_jobs_details_tag(self, tag, job_details):
        return [' '.join(job_detail.get(tag).split()) for job_detail in job_details]

    def get_page_cap(self, element_locator, element):
        element = self.soup.find(element_locator, element)
        return element.text if element else None

    def get_county(self, city):
        return get_county(city)

    def create_jobs_dict(self, job_title, job_url, job_country, job_city, remote='on-site', county=None):
        """
        Create the job dictionary for the future api
        """
        # Define a list for counties in case there is more than one
        self.counties = []
        
        if not county:
            # Get the county using the city
            if type(job_city) == list:
                for city in job_city:
                    self.counties.append(self.get_county(city))
                job_county = self.counties
            else:
                job_county = self.get_county(job_city)
        else:
            job_county = county
                    
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

