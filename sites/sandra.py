#
#
#
# sandra > https://www.sandra.ro/job-uri

from sites.website_scraper_bs4 import BS4Scraper

class sandraScrapper(BS4Scraper):
    
    """
    A class for scraping job data from sandra website.
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
        Scrape job data from sandra website.
        """

        # Get the jobs
        job_titles_elements = self.get_jobs_elements('class_', "d-block job-name")
        job_url_elements = self.get_jobs_elements('class_', "waves-effect waves-light mdw-btn-outlined--secondary mdw-btn--cta application-button")
        
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)
        

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
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    URL = 'https://www.sandra.ro/job-uri'
    URL_LOGO = 'https://www.sandra.ro/@@poi.imageproxy/dee829ad349d413cb021a58367333415/dealer-logo.svg'
    company_name = 'sandra'
    sandra = sandraScrapper(company_name, URL, URL_LOGO)
    sandra.get_response()
    sandra.scrape_jobs()
    sandra.send_to_viitor()
    
    

