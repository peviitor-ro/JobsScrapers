#
#
#
#
## LeoHR > https://www.leohr.ro/jobs

from sites.website_scraper_bs4 import BS4Scraper

class LeohrScraper(BS4Scraper):
    
    """
    A class for scraping job data from LeoHr website.
    """
    url = 'https://www.leohr.ro/jobs'
    url_logo = 'https://www.leohr.ro/images/firma-de-recrutare.png'
    company_name = 'Leohr'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Softlead website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'section.section-60.section-md-50 h6 > a')
        job_urls_elements = self.get_jobs_elements('class_', 'buton-job')
        job_cities_elements = self.get_jobs_elements('css_', "div.page > main > section > div > div > div > div > div > p")    
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)
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
    
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "Romania", job_city.replace("Bucharest", "Bucuresti").split(", "))
            
            

if __name__ == "__main__":
    Leohr = LeohrScraper()
    Leohr.get_response()
    Leohr.scrape_jobs()
    Leohr.sent_to_future()
    
    

