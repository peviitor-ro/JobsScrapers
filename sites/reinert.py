#
#
#
# reinert > https://reinert-romania.ro/ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class reinertScrapper(BS4Scraper):
    
    """
    A class for scraping job data from reinert website.
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
        Scrape job data from reinert website.
        """

        job_elements = self.get_jobs_elements('css_', 'li > span > strong')
        
        self.job_titles = self.get_jobs_details_text(job_elements)

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
            self.create_jobs_dict(job_title, self.url, "România", "Oradea")

if __name__ == "__main__":
    URL = 'https://reinert-romania.ro/ro/cariere/'
    URL_LOGO = 'https://reinert-romania.ro/images/logo/reinert-main.png'
    company_name = 'reinert'
    reinert = reinertScrapper(company_name, URL, URL_LOGO)
    reinert.get_response()
    reinert.scrape_jobs()
    reinert.sent_to_future()
    
    

