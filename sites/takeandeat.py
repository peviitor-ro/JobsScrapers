#
#
#
# takeandeat > https://www.takeandeat.ro/cariera.html

from sites.website_scraper_bs4 import BS4Scraper

class takeandeatScraper(BS4Scraper):
    
    """
    A class for scraping job data from takeandeat website.
    """
    
    url = 'https://takeandeat.ro/cariere/'
    url_logo = 'https://static.takeaway.com/images/restaurants/ro/N55QQ3Q/logo_465x320.png'
    company_name = 'takeandeat'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from takeandeat website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "elementor-heading-title elementor-size-large")
        job_url_elements = self.get_jobs_elements('class_', 'elementor-button elementor-button-link elementor-size-sm')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)

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
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    takeandeat = takeandeatScraper()
    takeandeat.get_response()
    takeandeat.scrape_jobs()
    takeandeat.sent_to_future()
    
    

