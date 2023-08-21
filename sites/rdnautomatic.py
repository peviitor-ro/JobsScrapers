#
#
#
# rdnautomatic > https://www.rndautomatic.com/en/Career.html

from sites.website_scraper_bs4 import BS4Scraper

class rdnautomaticScrapper(BS4Scraper):
    
    """
    A class for scraping job data from rdnautomatic website.
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
        Scrape job data from rdnautomatic website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'job-title')
        job_cities_elements = self.get_jobs_elements('class_', "job-location")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)

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
            self.create_jobs_dict(job_title, self.url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://www.rndautomatic.com/en/Career.html'
    URL_LOGO = 'https://www.rndautomatic.com/images/logo/rndlogo.png'
    company_name = 'rdnautomatic'
    rdnautomatic = rdnautomaticScrapper(company_name, URL, URL_LOGO)
    rdnautomatic.get_response()
    rdnautomatic.scrape_jobs()
    rdnautomatic.sent_to_future()
    
    

