#
#
#
# rdnautomatic > https://www.rndautomatic.com/en/Career.html

from sites.website_scraper_bs4 import BS4Scraper

class rdnautomaticScraper(BS4Scraper):
    
    """
    A class for scraping job data from rdnautomatic website.
    """
    url = 'https://www.rndautomatic.com/en/Career.html'
    url_logo = 'https://www.rndautomatic.com/images/logo/rndlogo.png'
    company_name = 'rdnautomatic'
    
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
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name
    
    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city in zip(self.job_titles, self.job_cities):
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", job_city)
            self.job_count += 1

if __name__ == "__main__":
    rdnautomatic = rdnautomaticScraper()
    rdnautomatic.get_response()
    rdnautomatic.scrape_jobs()
    rdnautomatic.sent_to_future()
    
    

