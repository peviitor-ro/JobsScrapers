#
#
#
# c-scale > https://www.c-scale.ro/careers

from website_scraper_bs4 import BS4Scraper

class CScaleScrapper(BS4Scraper):
    
    """
    A class for scraping job data from c-scale website.
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
        Scrape job data from c-scale website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div > h2')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)

        self.format_data()
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            self.create_jobs_dict(job_title, "https://www.c-scale.ro/careers", "Romania", "Craiova")

if __name__ == "__main__":
    URL = 'https://www.c-scale.ro/careers'
    URL_LOGO = 'https://www.c-scale.ro/images/logo.png'
    company_name = 'cscale'
    cscale = CScaleScrapper(company_name, URL, URL_LOGO)
    cscale.get_response()
    cscale.scrape_jobs()
    
    

