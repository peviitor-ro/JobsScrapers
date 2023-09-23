#
#
#
# jobshop > https://www.jobshop.bestis.ro/joburi/

from sites.website_scraper_bs4 import BS4Scraper

class jobshopScraper(BS4Scraper):
    
    """
    A class for scraping job data from jobshop website.
    """
    url = 'https://www.jobshop.bestis.ro/joburi/'
    url_logo = 'https://www.jobshop.bestis.ro/wp-content/uploads/2023/02/logo_jobshop_negru_rgb-2-e1677414124685.png'
    company_name = 'jobshop'
    
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from jobshop website.
        """

        job_title_elements = self.get_jobs_elements('css_', "h3[class='elementor-heading-title elementor-size-default']")
        job_urls_elements = self.get_jobs_elements('css_', "a[class='elementor-button-link elementor-button elementor-size-md']")
        job_cities_elements = self.get_jobs_elements('css_', "h5[class='elementor-heading-title elementor-size-default']")
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)[:-1]
        self.job_urls = self.get_jobs_details_href(job_urls_elements)[1::2]
        self.job_cities = self.get_jobs_details_text(job_cities_elements)[1::2]

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
            job_city = job_city.split("•")[1][1:]
            job_url = f"https://www.jobshop.bestis.ro{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    jobshop = jobshopScraper()
    jobshop.get_response()
    jobshop.scrape_jobs()
    jobshop.sent_to_future()
    
    

