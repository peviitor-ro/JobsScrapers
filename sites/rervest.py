#
#
#
# rervest > https://rervest.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class rervestScraper(BS4Scraper):
    
    """
    A class for scraping job data from rervest website.
    """
    url = 'https://rervest.ro/cariere/'
    url_logo = 'https://rervest.ro/wp-content/uploads/2018/02/rervest-01.svg'
    company_name = 'rervest'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
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
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    rervest = rervestScraper()
    rervest.get_response()
    rervest.scrape_jobs()
    rervest.sent_to_future()
    
    

