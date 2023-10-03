#
#
#
# eurotech > https://eurotech-iasi.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class eurotechScraper(BS4Scraper):
    
    """
    A class for scraping job data from eurotech website.
    """
    url = 'https://eurotech-iasi.ro/cariere/'
    url_logo = 'https://eurotech-iasi.ro/wp-content/uploads/2020/07/eurotech-iasi.ro-main-logo.svg'
    company_name = 'eurotech'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from eurotech website.
        """

        job_elements = self.get_jobs_elements('css_', "div > div.media-body.rtin-content-area > h3 > a")
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)

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
    eurotech = eurotechScraper()
    eurotech.get_response()
    eurotech.scrape_jobs()
    eurotech.sent_to_future()
    
    

