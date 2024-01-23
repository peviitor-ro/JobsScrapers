#
#
#
# reginamaria > https://cariere.reginamaria.ro/jobs?search=&p=1000

from sites.website_scraper_bs4 import BS4Scraper

class reginamariaScraper(BS4Scraper):
    
    """
    A class for scraping job data from reginamaria website.
    """
    url = 'https://cariere.reginamaria.ro/jobs?search=&p=1000'
    url_logo = 'https://www.reginamaria.ro/themes/custom/regina_maria/logo.svg'
    company_name = 'reginamaria'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from reginamaria website.
        """

        job_elements = self.get_jobs_elements('css_', 'div.theTitle > a')
        job_city_elements = self.get_jobs_elements('css_', 'div > ul > li:nth-child(5)')
        
        self.job_cities = self.get_jobs_details_text(job_city_elements)
        self.job_titles = self.get_jobs_details_text(job_elements)
            
        self.job_urls = self.get_jobs_details_href(job_elements)

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
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace("Locatie ", ""))

if __name__ == "__main__":
    reginamaria = reginamariaScraper()
    reginamaria.get_response()
    reginamaria.scrape_jobs()
    reginamaria.sent_to_future()
    
    

