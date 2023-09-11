#
#
#
# iuliuscompany > https://cariere.iuliuscompany.ro/

from sites.website_scraper_bs4 import BS4Scraper

class iuliuscompanyScrapper(BS4Scraper):
    
    """
    A class for scraping job data from iuliuscompany website.
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
        Scrape job data from iuliuscompany website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "div > div > div > div.poza-oferta > div.persoana-oferta > a > img")
        job_location_elements = self.get_jobs_elements('class_', "locatie")
        job_url_elements = self.get_jobs_elements('css_', 'div > div > div > div.poza-oferta > div.persoana-oferta > a')
        
        self.job_titles = self.get_jobs_details_tag('alt', job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_location_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = self.url + job_url
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace("LOCAȚIE: ", ""))

if __name__ == "__main__":
    URL = 'https://cariere.iuliuscompany.ro'
    URL_LOGO = 'https://cariere.iuliuscompany.ro/images/iulius-mall.svg'
    company_name = 'iuliuscompany'
    iuliuscompany = iuliuscompanyScrapper(company_name, URL, URL_LOGO)
    iuliuscompany.get_response()
    iuliuscompany.scrape_jobs()
    iuliuscompany.sent_to_future()
    
    

