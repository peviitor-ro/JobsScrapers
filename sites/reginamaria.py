#
#
#
# reginamaria > https://cariere.reginamaria.ro/jobs

import time
import requests
from bs4 import BeautifulSoup
from sites.website_scraper_bs4 import BS4Scraper


class reginamariaScraper(BS4Scraper):
    
    """
    A class for scraping job data from reginamaria website.
    """
    url = 'https://cariere.reginamaria.ro/jobs'
    url_logo = 'https://www.reginamaria.ro/themes/custom/regina_maria/logo.svg'
    company_name = 'reginamaria'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self._set_headers()
                response = requests.get(self.url, headers=self.DEFAULT_HEADERS, verify=False, timeout=30)
                self.soup = BeautifulSoup(response.content, 'lxml')
                return True
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError,
                    requests.exceptions.Timeout, requests.exceptions.RequestException) as e:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    print(f"Warning: Could not connect to {self.url}: {e}")
                    self.soup = BeautifulSoup("", "lxml")
                    return False
        return False
    
    def scrape_jobs(self):
        """
        Scrape job data from reginamaria website using API.
        """

        self.job_titles = []
        self.job_urls = []
        self.job_cities = []
        
        page = 1
        max_retries = 3
        while True:
            for attempt in range(max_retries):
                try:
                    response = requests.get(f'https://cariere.reginamaria.ro/jobs/load?page={page}', headers=self.DEFAULT_HEADERS, verify=False, timeout=30)
                    data = response.json()
                    break
                except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError,
                        requests.exceptions.Timeout, requests.exceptions.RequestException) as e:
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                    else:
                        print(f"Warning: Could not fetch page {page} from API: {e}")
                        data = {"data": {"jobs": []}}
            
            jobs = data.get('data', {}).get('jobs', [])
            if not jobs:
                break
                
            for job in jobs:
                self.job_titles.append(job.get('title', ''))
                self.job_urls.append(job.get('url', ''))
                city_data = job.get('city', [])
                if city_data and isinstance(city_data, list):
                    city = city_data[0].get('name', '') if city_data else ''
                else:
                    city = ''
                self.job_cities.append(city)
            
            page += 1

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    reginamaria = reginamariaScraper()
    reginamaria.get_response()
    reginamaria.scrape_jobs()
    reginamaria.sent_to_future()
    
    

