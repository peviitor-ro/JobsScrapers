#
#
#
# Cargus > https://www.cargus.ro/careers-ro/

from sites.website_scraper_bs4 import BS4Scraper

class CargusScraper(BS4Scraper):
    
    """
    A class for scraping job data from Cargus website.
    """
    url = 'https://www.cargus.ro/careers-ro/'
    url_logo = 'https://www.cargus.ro/wp-content/uploads/logo-cargus.png'
    company_name = 'Cargus'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Cargus website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div > h3')
        job_cities_elements = self.get_jobs_elements('css_', 'div > h2 > strong > mark')
        job_urls_elements = self.get_jobs_elements('css_', "div > div > div > div > div > div > a")[2:]
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

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
            if job_city == "Național":
                job_city = ["all"]

            county = "Ilfov" if "Măgurele" in job_city else None
            
            self.create_jobs_dict(job_title, job_url, "România", job_city, "On-site", county)

if __name__ == "__main__":
    Cargus = CargusScraper()
    Cargus.get_response()
    Cargus.scrape_jobs()
    Cargus.sent_to_future()
    
    

