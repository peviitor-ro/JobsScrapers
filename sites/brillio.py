#
#
#
# brillio > https://careers.brillio.com/job-listing/?job_title=&country=Romania&workplace=


from sites.website_scraper_bs4 import BS4Scraper

class brillioScrapper(BS4Scraper):
    
    """
    A class for scraping job data from brillio website.
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
        Scrape job data from brillio website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "div > div > h4")
        job_location_elements = self.get_jobs_elements('css_', 'div > div > p.infoline > span:nth-child(1)')
        job_urls_elements = self.get_jobs_elements('css_', "a[href^='https://careers.brillio.com/job-details?job-id=']")
        
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
    URL = 'https://careers.brillio.com/job-listing/?job_title=&country=Romania&workplace='
    URL_LOGO = 'https://careers.brillio.com/wp-content/themes/brilliotheme/assets/Brillio_Primary-Logo_12.2021.svg'
    company_name = 'brillio'
    brillio = brillioScrapper(company_name, URL, URL_LOGO)
    brillio.get_response()
    brillio.scrape_jobs()
    brillio.sent_to_future()
    
    

