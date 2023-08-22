#
#
#
# splendor > https://www.splendor.ro/cariera.html

from sites.website_scraper_bs4 import BS4Scraper

class splendorScrapper(BS4Scraper):
    
    """
    A class for scraping job data from splendor website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        self.job_count = 1
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from splendor website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "div.job_item_tit.js_jit_trigger > h5")
        job_location_elements = self.get_jobs_elements('css_', 'div.job_item_tit.js_jit_trigger > p')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_location_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city in zip(self.job_titles, self.job_cities):
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", job_city[18:].replace(".", "").split(","))
            self.job_count += 1

if __name__ == "__main__":
    URL = 'https://www.splendor.ro/cariera.html'
    URL_LOGO = 'https://www.splendor.ro/webroot/img/logo/splendor_logo1.png'
    company_name = 'splendor'
    splendor = splendorScrapper(company_name, URL, URL_LOGO)
    splendor.get_response()
    splendor.scrape_jobs()
    splendor.sent_to_future()
    
    

