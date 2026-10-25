#
#
#
# velpitar > https://velpitar.ro/cariere-vel-pitar/

import time
import requests
from bs4 import BeautifulSoup
from sites.website_scraper_bs4 import BS4Scraper

class velpitarScraper(BS4Scraper):
    
    """
    A class for scraping job data from velpitar website.
    """
    url = 'https://www.ejobs.ro/company/vel-pitar/5195'
    url_logo = 'https://velpitar.ro/wp-content/uploads/2023/05/cropped-Backup_of_Sigla-Finala-fara-spate-CMYK.png'
    company_name = 'velpitar'
    
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
                self.DEFAULT_HEADERS['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
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
        Scrape job data from velpitar website.
        """

        job_elements = self.get_jobs_elements('css_', 'li.job-card-wrapper')

        self.job_titles = []
        self.job_urls = []
        self.job_cities = []
        seen_urls = set()

        for job_element in job_elements:
            title_element = job_element.select_one('a[data-testid="b2c-job-card-title-link"]')
            if not title_element:
                continue

            job_url = title_element.get('href')
            if not job_url or job_url in seen_urls:
                continue
            seen_urls.add(job_url)

            location_element = job_element.select_one('.job-card-content-middle__info:not(.job-card-content-middle__info--darker)')
            location = ' '.join(location_element.get_text(' ', strip=True).split()) if location_element else ''
            cities = [city.strip() for city in location.split(',') if self.get_county(city.strip())]

            self.job_titles.append(' '.join(title_element.get_text(' ', strip=True).split()))
            self.job_urls.append(f'https://www.ejobs.ro{job_url}')
            self.job_cities.append(cities if cities else [location])

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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    velpitar = velpitarScraper()
    velpitar.get_response()
    velpitar.scrape_jobs()
    velpitar.sent_to_future()
    
    

