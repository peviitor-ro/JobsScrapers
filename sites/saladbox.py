#
#
#
# saladbox > https://saladbox.ro/ro/cariere

from sites.website_scraper_bs4 import BS4Scraper

class saladboxScrapper(BS4Scraper):
    
    """
    A class for scraping job data from saladbox website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from saladbox website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'career-position-link js-open-career-detail-modal')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            self.create_jobs_dict(job_title, self.url, "România", "România")

if __name__ == "__main__":
    URL = 'https://saladbox.ro/ro/cariere'
    URL_LOGO = 'https://saladbox.ro/images/layout/logo.png'
    company_name = 'saladbox'
    saladbox = saladboxScrapper(company_name, URL, URL_LOGO)
    saladbox.get_response()
    saladbox.scrape_jobs()
    saladbox.sent_to_future()
    
    

