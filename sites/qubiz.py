#
#
#
#
## Qubiz > https://www.qubiz.com/jobs

from sites.website_scraper_bs4 import BS4Scraper

class QubizScraper(BS4Scraper):
    
    """
    A class for scraping job data from Qubiz website.
    """
    url = 'https://www.qubiz.com/jobs'
    url_logo = 'https://assets-global.website-files.com/603e16fd5761f8f7787bf39a/64491d149607dd73d0e80235_LogoWebsiteAnniversary.svg'
    company_name = 'Qubiz'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Qubiz website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'head-2-job-title')
        job_urls_elements = self.get_jobs_elements('class_', 'button-blue---job-openings w-button')
        job_cities_elements = self.get_jobs_elements('class_', 'text-block-12')
        
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
        job_country = "Romania"
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, job_country, job_city, remote='on-site', county=None)

if __name__ == "__main__":
    Qubiz = QubizScraper()
    Qubiz.get_response()
    Qubiz.scrape_jobs()
   # Qubiz.sent_to_future()
    
    

