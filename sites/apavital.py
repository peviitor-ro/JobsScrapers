#
#
#
# apavital > https://www.apavital.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class apavitalScraper(BS4Scraper):
    
    """
    A class for scraping job data from apavital website.
    """
    url = 'https://www.apavital.ro/cariere'
    url_logo = 'https://www.apavital.ro/assets/images/logo.png'
    company_name = 'apavital'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from apavital website.
        """
        page_counter = 1
        job_elements = self.get_jobs_elements('css_', "#cariere > div.simple-page.b > div > div > div.water-boxes.careers-boxes > div > div.water-box-title > a")
        self.job_titles = []
        self.job_urls = []
        
        while job_elements:
            self.job_titles.extend(self.get_jobs_details_text(job_elements))
            self.job_urls.extend(self.get_jobs_details_href(job_elements))
            
            page_counter += 1
            self.get_content(f"https://www.apavital.ro/cariere?page={page_counter}")
            job_elements = self.get_jobs_elements('css_', "#cariere > div.simple-page.b > div > div > div.water-boxes.careers-boxes > div > div.water-box-title > a")
        
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
            job_url = f"https://www.apavital.ro{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    apavital = apavitalScraper()
    apavital.get_response()
    apavital.scrape_jobs()
    apavital.sent_to_future()
    
    

