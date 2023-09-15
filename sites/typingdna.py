#
#
#
# typingdna > https://www.typingdna.com/careers


from sites.website_scraper_bs4 import BS4Scraper

class typingdnaScraper(BS4Scraper):
    
    """
    A class for scraping job data from typingdna website.
    """
    url = 'https://www.typingdna.com/careers'
    url_logo = 'https://www.typingdna.com/assets/images/typingdna-logo-blue.svg'
    company_name = 'typingdna'
    
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
        Scrape job data from typingdna website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "careers__job-title")
        job_location_elements = self.get_jobs_elements('class_', 'careers__job-location')
        # job_urls_elements = self.get_jobs_elements('class_', "tdna-btn tdna-primary-btn careers__job_application-button")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_location_elements)
        # self.job_urls = self.get_jobs_details_href(job_urls_elements)

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
            job_city = job_city.split()[0][:-1]
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", job_city)
            self.job_count += 1

if __name__ == "__main__":
    typingdna = typingdnaScraper()
    typingdna.get_response()
    typingdna.scrape_jobs()
    typingdna.sent_to_future()
    
    

