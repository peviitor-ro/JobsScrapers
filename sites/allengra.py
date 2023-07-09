#
#
#
# allengra > https://allengra.eu/career.php


from sites.website_scraper_bs4 import BS4Scraper

class allengraScrapper(BS4Scraper):
    
    """
    A class for scraping job data from allengra website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.website_url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.website_url)
    
    def scrape_jobs(self):
        """
        Scrape job data from allengra website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "div > div > h4")

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
            self.create_jobs_dict(job_title, self.website_url, "România", "Oradea")

if __name__ == "__main__":
    URL = 'https://allengra.eu/career.php'
    URL_LOGO = 'https://allengra.eu/images/logo_allengra%20(2).svg'
    company_name = 'allengra'
    allengra = allengraScrapper(company_name, URL, URL_LOGO)
    allengra.get_response()
    allengra.scrape_jobs()
    allengra.sent_to_future()
    
    

