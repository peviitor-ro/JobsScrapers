#
#
#
#
## vetro > https://vetro.vet/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class vetroScraper(BS4Scraper):
    
    """
    A class for scraping job data from vetro website.
    """
    url = 'https://vetro.vet/cariere/'
    url_logo = 'https://vetro.vet/wp-content/uploads/2020/08/Logo_Vetro-2048x550.png'
    company_name = 'vetro'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from vetro website.
        """

        job_elements = self.get_jobs_elements('css_', 'section.elementor-section.elementor-top-section.elementor-element.elementor-element-31c883d.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > section > div > div > div > div > div > h2')
        job_urls_elements = self.get_jobs_elements('class_', 'elementor-button elementor-button-link elementor-size-sm')

        self.job_titles = self.get_jobs_details_text(job_elements)[::2]
        self.job_cities = self.get_jobs_details_text(job_elements)[1::2]
                                         
        self.job_urls = [job_url for job_url in self.get_jobs_details_href(job_urls_elements) if job_url.startswith('https://vetro.vet/cariere')]

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
    vetro = vetroScraper()
    vetro.get_response()
    vetro.scrape_jobs()
    vetro.sent_to_future()
    
    

