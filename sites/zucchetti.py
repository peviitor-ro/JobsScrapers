#
#
#
# zucchetti > https://www.zucchettiromania.com/romania/cms/careers.html

from sites.website_scraper_bs4 import BS4Scraper

class zucchettiScrapper(BS4Scraper):
    
    """
    A class for scraping job data from zucchetti website.
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
        Scrape job data from zucchetti website.
        """

        job_elements = self.get_jobs_elements('css_', "a[href^='http://www.zucchettiromania.com/romania/dms/']:not([target='_blank'])")
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Oradea")

if __name__ == "__main__":
    URL = 'https://www.zucchettiromania.com/romania/cms/careers.html'
    URL_LOGO = 'https://www.zucchettiromania.com/romania/templates/romania/img/logo.png'
    company_name = 'zucchetti'
    zucchetti = zucchettiScrapper(company_name, URL, URL_LOGO)
    zucchetti.get_response()
    zucchetti.scrape_jobs()
    zucchetti.sent_to_future()
    

