#
#
#
# Beenear > https://www.beenear.com/career/

from sites.website_scraper_bs4 import BS4Scraper

class BeenearScraper(BS4Scraper):
    
    """
    A class for scraping job data from Beenear website.
    """
    url = 'https://www.beenear.com/career/'
    url_logo = 'https://beenear.com/wp-content/uploads/2020/07/logo.svg'
    company_name = 'Beenear'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Beenear website.
        """
        job_titles_elements = self.get_jobs_elements('css_', 'div > h3 > a')
        job_urls_elements = self.get_jobs_elements('css_', "div > h3 > a")
        
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
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    Beenear = BeenearScraper()
    Beenear.get_response()
    Beenear.scrape_jobs()
    Beenear.sent_to_future()
    
    

