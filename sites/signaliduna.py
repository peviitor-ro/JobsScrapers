#
#
#
# signaliduna > https://www.signal-iduna.ro/ro/cariere

from sites.website_scraper_bs4 import BS4Scraper

class signalidunaScraper(BS4Scraper):
    
    """
    A class for scraping job data from signaliduna website.
    """
    url = 'https://www.signal-iduna.ro/ro/cariere'
    url_logo = 'https://www.signal-iduna.ro/images/og_image_v1.jpg'
    company_name = 'signaliduna'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from signaliduna website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "h3.text-primary")
        job_urls_elements = self.get_jobs_elements('css_', "a[href*='/cariere/']")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
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
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Bucuresti")

if __name__ == "__main__":
    signaliduna = signalidunaScraper()
    signaliduna.get_response()
    signaliduna.scrape_jobs()
    signaliduna.sent_to_future()
    
    

