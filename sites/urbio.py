#
#
#
# urbio > https://urbio.ai/careers/

import re
import time
import requests
from bs4 import BeautifulSoup
from sites.website_scraper_bs4 import BS4Scraper

class urbioScraper(BS4Scraper):
    
    """
    A class for scraping job data from urbio website.
    """
    url = 'https://urbio.ai/careers/'
    url_logo = 'https://urbio.ai/wp-content/uploads/2026/08/Logo_Urbio_V2-1-1024x284.png'
    company_name = 'urbio'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
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
    
    def get_tab_countries(self):
        """
        Map each tab panel id to the country stored in its tab title.
        """
        countries = {}
        for button in self.get_jobs_elements('css_', 'button.e-n-tab-title'):
            target = button.get('aria-controls')
            if target:
                countries[target] = ' '.join(button.get_text().split())
        return countries

    def get_romanian_city(self, department, job_title):
        """
        The city is embedded in the department and/or the job title. Pick the
        last token that matches a known Romanian locality.
        """
        candidates = re.split(r'\s*[-,]\s*', f"{department} - {job_title}")
        for candidate in reversed(candidates):
            candidate = candidate.strip()
            if candidate and self.get_county(candidate):
                return candidate
        return None

    def scrape_jobs(self):
        """
        Scrape job data from urbio website.
        """
        self.job_titles = []
        self.job_countries = []
        self.job_cities = []

        tab_countries = self.get_tab_countries()

        for panel in self.get_jobs_elements('css_', 'div[role="tabpanel"]'):
            tab_country = tab_countries.get(panel.get('id'), '')
            country = 'România' if tab_country == 'Romania' else tab_country

            for heading in panel.select('h2.elementor-heading-title'):
                if ' '.join(heading.get_text().split()) != 'Available':
                    continue

                title_heading = heading.find_previous('h2', class_='elementor-heading-title')
                if title_heading is None:
                    continue
                job_title = ' '.join(title_heading.get_text().split())

                department_heading = title_heading.find_previous('h2', class_='elementor-heading-title')
                department = ' '.join(department_heading.get_text().split()) if department_heading else ''

                self.job_titles.append(job_title)
                self.job_countries.append(country)

                if country == 'România':
                    self.job_cities.append(self.get_romanian_city(department, job_title) or country)
                else:
                    self.job_cities.append(country)

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
        for job_title, job_country, job_city in zip(self.job_titles, self.job_countries, self.job_cities):
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, job_country, job_city)
            self.job_count += 1

if __name__ == "__main__":
    urbio = urbioScraper()
    urbio.get_response()
    urbio.scrape_jobs()
    urbio.sent_to_future()
    
    
