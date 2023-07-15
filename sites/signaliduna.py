#
#
#
# signaliduna > https://www.signal-iduna.ro/cariere

from sites.website_scraper_bs4 import BS4Scraper

class signalidunaScrapper(BS4Scraper):
    
    """
    A class for scraping job data from signaliduna website.
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
        Scrape job data from signaliduna website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "h4[class='title']")
        job_urls_elements = self.get_jobs_elements('css_', "div > div:nth-child(2) > div > div > a")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

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
            self.create_jobs_dict(job_title, job_url, "România", "Bucuresti")

if __name__ == "__main__":
    URL = 'https://www.signal-iduna.ro/cariere'
    URL_LOGO = 'https://www.signal-iduna.ro/images/og_image_v1.jpg'
    company_name = 'signaliduna'
    signaliduna = signalidunaScrapper(company_name, URL, URL_LOGO)
    signaliduna.get_response()
    signaliduna.scrape_jobs()
    signaliduna.sent_to_future()
    
    

