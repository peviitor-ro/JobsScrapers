from website_scraper_bs4 import BS4Scraper
from math import ceil

class CargusScrapper(BS4Scraper):
    
    """
    A class for scraping job data from Cargus website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(company_name, url, company_logo_url)
        
    def get_response(self):
        self.get_content()
    
    def scrape_jobs(self):
        """
        Scrape job data from Cargus website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div.jobOpis > p:nth-child(1) > strong')
        job_cities_elements = self.get_jobs_elements('css_', 'div.jobInfo > p:nth-child(2)')
        job_urls_elements = self.get_jobs_elements('css_', "a[class='btn1']")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

        self.format_data()
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            if job_title and job_city and job_url:
                self.create_jobs_dict(job_title, job_url, "Romania", job_city)

if __name__ == "__main__":
    URL = 'https://www.cargus.ro/careers-ro/'
    URL_LOGO = 'https://www.cargus.ro/wp-content/uploads/logo-cargus.png'
    company_name = 'Cargus'
    Cargus = CargusScrapper(company_name, URL, URL_LOGO)
    Cargus.get_response()
    Cargus.scrape_jobs()
    
    

