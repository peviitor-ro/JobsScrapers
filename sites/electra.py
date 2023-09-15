#
# 
#
# electra > https://www.electra.ro/ro/cariere


from sites.website_scraper_bs4 import BS4Scraper

class electraScraper(BS4Scraper):
    
    """
    A class for scraping job data from electra website.
    """
    url = 'https://www.electra.ro/ro/cariere'
    url_logo = 'https://www.electra.ro/images/layout/electra-logo.png'
    company_name = 'electra'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from electra website.
        """

        job_title_elements = self.get_jobs_elements('css_', 'div.container.main-content > div > div > div > div > div > div > h4 > b')
        job_url_elements = self.get_jobs_elements('class_', 'btn btn-secondary')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)
        
        
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
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            job_url = self.url + job_url.replace("/ro/cariere", "")
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    electra = electraScraper()
    electra.get_response()
    electra.scrape_jobs()
    electra.sent_to_future()
    
    

