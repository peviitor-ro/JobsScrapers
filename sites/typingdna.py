#
#
#
# typingdna > https://www.typingdna.com/careers


from sites.website_scraper_bs4 import BS4Scraper

class typingdnaScrapper(BS4Scraper):
    
    """
    A class for scraping job data from typingdna website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.website_url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.website_url)
    
    def scrape_jobs(self):
        """
        Scrape job data from typingdna website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "careers__job-title")
        job_location_elements = self.get_jobs_elements('class_', 'careers__job-location')
        job_urls_elements = self.get_jobs_elements('class_', "tdna-btn tdna-primary-btn careers__job_application-button")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_location_elements)
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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_city = job_city.split()[0][:-1]
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://www.typingdna.com/careers'
    URL_LOGO = 'https://www.typingdna.com/assets/images/typingdna-logo-blue.svg'
    company_name = 'typingdna'
    typingdna = typingdnaScrapper(company_name, URL, URL_LOGO)
    typingdna.get_response()
    typingdna.scrape_jobs()
    typingdna.sent_to_future()
    
    

