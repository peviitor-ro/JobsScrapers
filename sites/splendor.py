#
#
#
# splendor > https://www.splendor.ro/cariera.html

from sites.website_scraper_bs4 import BS4Scraper

class splendorScraper(BS4Scraper):
    
    """
    A class for scraping job data from splendor website.
    """
    url = 'https://www.splendor.ro/cariera.html'
    url_logo = 'https://www.splendor.ro/webroot/img/logo/splendor_logo1.png'
    company_name = 'splendor'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)
        
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
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city in zip(self.job_titles, self.job_cities):
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", job_city[18:].replace(".", "").split(","))
            self.job_count += 1

if __name__ == "__main__":
    splendor = splendorScraper()
    splendor.get_response()
    splendor.scrape_jobs()
    splendor.sent_to_future()
    
    

