#
#
#
# rervest > https://rervest.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class rervestScrapper(BS4Scraper):
    
    """
    A class for scraping job data from rervest website.
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
        Scrape job data from rervest website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'job-title')
        job_urls_elements = self.get_jobs_elements('css_', "div > div.job-list > div > a")
        
        unformatted_job_data = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = []
        self.job_titles = []
        
        # Itterate over job title and split the city and title apart
        for job_data in unformatted_job_data:
            self.job_cities.append(job_data.split(": ")[0])
            self.job_titles.append(job_data.split(": ")[1])
            
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

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
            self.create_jobs_dict(job_title, job_url, "România", "Oradea")

if __name__ == "__main__":
    URL = 'https://rervest.ro/cariere/'
    URL_LOGO = 'https://rervest.ro/wp-content/uploads/2018/02/rervest-01.svg'
    company_name = 'rervest'
    rervest = rervestScrapper(company_name, URL, URL_LOGO)
    rervest.get_response()
    rervest.scrape_jobs()
    rervest.sent_to_future()
    
    

