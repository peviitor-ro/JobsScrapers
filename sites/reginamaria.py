#
#
#
# reginamaria > https://cariere.reginamaria.ro/jobs

import requests
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
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from reginamaria website using API.
        """

        self.job_titles = []
        self.job_urls = []
        self.job_cities = []
        
        page = 1
        while True:
            response = requests.get(f'https://cariere.reginamaria.ro/jobs/load?page={page}', headers=self.DEFAULT_HEADERS)
            data = response.json()
            
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
    
    

