#
#
#
# Orange > https://orangeromania-careerpage.kariera.pro/jobs.feed.json


import requests
from sites.website_scraper_bs4 import BS4Scraper


class OrangeScraper(BS4Scraper):
    
    """
    A class for scraping job data from Orange website.
    """
    url = 'https://orangeromania-careerpage.kariera.pro/jobs.feed.json'
    url_logo = 'https://www.orange.ro/imagini/orange-logo-static.svg'
    company_name = 'Orange'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        response = requests.get(self.url, verify=False, timeout=30, headers={'Accept': 'application/json'})
        self.json_data = response.json()
    
    def scrape_jobs(self):
        """
        Scrape job data from Orange website.
        """
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        
        items = self.json_data.get('dataFeedElement', [])
        
        for item in items:
            job = item.get('item', {})
            location = job.get('jobLocation', {}).get('address', {})
            country = location.get('addressCountry', '')
            city = location.get('addressLocality', '')
            
            # Filter for Romania jobs
            if country == 'Rumunia':
                title = job.get('title', '')
                job_url = job.get('url', '')
                
                # Normalize city names
                city = city.replace('Bucharest', 'Bucuresti')
                if city == 'Romania' or not city:
                    city = 'Bucuresti'
                
                self.job_titles.append(title)
                self.job_cities.append(city)
                self.job_urls.append(job_url)
        
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
    Orange = OrangeScraper()
    Orange.get_response()
    Orange.scrape_jobs()
    Orange.sent_to_future()
