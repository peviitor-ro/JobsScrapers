#
#
#
# Cargus > https://www.cargus.ro/careers-ro/

from sites.website_scraper_bs4 import BS4Scraper

class cargusScraper(BS4Scraper):
    
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
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        
        job_links = {
            'Colaboratori-curieri în rețeaua Cargus': ('https://www.cargus.ro/cariere/curieri-si-parteneri-pentru-activitatea-de-curierat/', 'Național'),
            'Contact Center Advisor': ('https://www.cargus.ro/cariere/contact-center-advisor/', 'Măgurele'),
            'Team Leader Curieri': ('https://www.cargus.ro/cariere/teamleader/', 'Național'),
        }
        
        for title, (url, city) in job_links.items():
            self.job_titles.append(title)
            self.job_cities.append(city)
            self.job_urls.append(url)

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
                job_city = "România"
                county = None
            else:
                county = "Ilfov" if "Măgurele" in job_city else None
            
            self.create_jobs_dict(job_title, job_url, "România", job_city, "On-site", county)

if __name__ == "__main__":
    Cargus = cargusScraper()
    Cargus.get_response()
    Cargus.scrape_jobs()
    Cargus.sent_to_future()
