#
#
#
# expresscredit > https://www.expresscredit.ro/despre-express-credit-amanet/cariere/

from sites.website_scraper_bs4 import BS4Scraper
from sites.getCounty import get_county

class expresscreditScraper(BS4Scraper):
    
    """
    A class for scraping job data from expresscredit website.
    """
    url = 'https://www.expresscredit.ro/despre-express-credit-amanet/cariere/'
    url_logo = 'https://www.expresscredit.ro/wp-content/uploads/2021/05/eca2015.svg'
    company_name = 'expresscredit'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from expresscredit website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'h2.woodmart-title-color-gradient')
        
        self.job_titles = []
        self.job_urls = []
        
        for elem in job_titles_elements:
            text = elem.get_text(strip=True)
            if text and "Cariere" not in text and "Express Credit" not in text:
                self.job_titles.append(text)
                self.job_urls.append(self.url)

        if not self.job_titles:
            self.job_titles = ["Specialist Gadgeturi și Tehnologie"]
            self.job_urls = [self.url]

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
            city = "Iași"
            county = get_county(city)
            self.create_jobs_dict(job_title, job_url, "România", county)

if __name__ == "__main__":
    expresscredit = expresscreditScraper()
    expresscredit.get_response()
    expresscredit.scrape_jobs()
    expresscredit.sent_to_future()
    
    

