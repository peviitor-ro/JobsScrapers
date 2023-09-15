#
#
#
# iuliuscompany > https://cariere.iuliuscompany.ro/

from sites.website_scraper_bs4 import BS4Scraper

class iuliuscompanyScraper(BS4Scraper):
    
    """
    A class for scraping job data from iuliuscompany website.
    """
    url = 'https://cariere.iuliuscompany.ro'
    url_logo = 'https://ami.cname.ro/_/company/iulius-group/mediaPool/uK2z1mO.jpg'
    company_name = 'iuliuscompany'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
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
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = self.url + job_url
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace("LOCAȚIE: ", ""))

if __name__ == "__main__":
    iuliuscompany = iuliuscompanyScraper()
    iuliuscompany.get_response()
    iuliuscompany.scrape_jobs()
    iuliuscompany.sent_to_future()
    
    

