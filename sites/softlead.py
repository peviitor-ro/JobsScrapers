#
#
#
#
## Softlead > https://softlead.ro/cariere

from sites.website_scraper_bs4 import BS4Scraper

class SoftleadScraper(BS4Scraper):
    
    """
    A class for scraping job data from Softlead website.
    """
    url = 'https://softlead.ro/cariere'
    url_logo = 'https://softlead.ro/frontendAssets/images/logo.webp'
    company_name = 'Softlead'
    base_url = 'https://softlead.ro'  # Define the base URL
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Softlead website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'blog-title')
        job_urls_elements = self.get_jobs_elements('class_', 'readmore')    
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

        # Convert relative URLs to absolute URLs
        self.job_urls = [self.base_url + job_url for job_url in self.job_urls]

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
            self.create_jobs_dict(job_title, job_url, "România", "Bucuresti")
            

if __name__ == "__main__":
    Softlead = SoftleadScraper()
    Softlead.get_response()
    Softlead.scrape_jobs()
    Softlead.sent_to_future()
    
    

