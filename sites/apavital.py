#
#
#
# apavital > https://www.apavital.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class apavitalScrapper(BS4Scraper):
    
    """
    A class for scraping job data from apavital website.
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
        Scrape job data from apavital website.
        """

        job_elements = self.get_jobs_elements('css_', "#cariere > div.simple-page.b > div > div > div.water-boxes.careers-boxes > div > div.water-box-title > a")
        
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
            job_url = f"https://www.apavital.ro{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", job_url)

if __name__ == "__main__":
    URL = 'https://www.apavital.ro/cariere'
    URL_LOGO = 'https://www.apavital.ro/assets/images/logo.png'
    company_name = 'apavital'
    apavital = apavitalScrapper(company_name, URL, URL_LOGO)
    apavital.get_response()
    apavital.scrape_jobs()
    apavital.sent_to_future()
    
    

