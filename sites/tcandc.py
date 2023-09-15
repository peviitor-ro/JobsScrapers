#
#
#
# tcandc > https://www.tcandc.com/company/career.html


from sites.website_scraper_bs4 import BS4Scraper

class tcandcScraper(BS4Scraper):
    
    """
    A class for scraping job data from tcandc website.
    """
    url = 'https://www.tcandc.com/company/career.html'
    url_logo = 'https://www.tcandc.com/templates/tcandc2020/images/tcandc-header-logo_light-2022_30y.png'
    company_name = 'tcandc'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from tcandc website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "a[href^='https://www.tcandc.com/company/career/']")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_titles_elements)

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
            self.create_jobs_dict(job_title, job_url, "România", "Oradea")

if __name__ == "__main__":
    tcandc = tcandcScraper()
    tcandc.get_response()
    tcandc.scrape_jobs()
    tcandc.sent_to_future()
    
    

