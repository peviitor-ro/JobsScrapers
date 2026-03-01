#
#
#
# sonrisatechnologies > https://www.careers.sonrisa.hu/

from sites.website_scraper_bs4 import BS4Scraper
from sites.getCounty import get_county

class sonrisatechnologiesScraper(BS4Scraper):
    
    """
    A class for scraping job data from sonrisatechnologies website.
    """
    url = 'https://www.careers.sonrisa.hu/#jobs'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/sonrisa.PNG'
    company_name = 'sonrisatechnologies'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from sonrisatechnologies website.
        """

        job_elements = self.get_jobs_elements('css_', 'li.border-b > div')
        
        self.job_titles = []
        self.job_urls = []
        self.job_cities = []
        
        for job in job_elements:
            title_elem = job.find('a')
            if title_elem:
                self.job_titles.append(title_elem.get_text(strip=True))
                self.job_urls.append(title_elem.get('href'))
            
            location_elem = job.find('span', title=True)
            if location_elem:
                location_text = location_elem.get('title', '')
                if location_text:
                    self.job_cities.append(location_text)
                else:
                    self.job_cities.append(location_elem.get_text(strip=True))
            else:
                self.job_cities.append("")

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
            if "Fully Remote" in job_title:
                remote = "remote"
            elif "Hybrid" in job_title:
                remote = "hybrid"
            else:
                remote = "on-site"
            
            self.create_jobs_dict(job_title, job_url, "România", job_city, remote)

if __name__ == "__main__":
    sonrisatechnologies = sonrisatechnologiesScraper()
    sonrisatechnologies.get_response()
    sonrisatechnologies.scrape_jobs()
    sonrisatechnologies.sent_to_future()
    
    

