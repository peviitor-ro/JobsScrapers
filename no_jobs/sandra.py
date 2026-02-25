#
#
#
# sandra > https://www.vag.sandra.ro/job-uri

from sites.website_scraper_bs4 import BS4Scraper

class sandraScraper(BS4Scraper):
    
    """
    A class for scraping job data from sandra website.
    """
    
    url = 'https://www.vag.sandra.ro/job-uri'
    url_logo = 'https://www.vag.sandra.ro/@@poi.imageproxy/00ac5c3b39d64291aebfb07397bf6020/dealer-logo.svg'
    company_name = 'sandra'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from sandra website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "job-name")
        job_url_elements = self.get_jobs_elements('class_', "application-button")
        
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        
        self.job_urls = []
        for job_url_element in job_url_elements:
            anchor = job_url_element.find('a')
            if anchor and anchor.get('href'):
                self.job_urls.append(anchor.get('href'))
            else:
                self.job_urls.append(job_url_element.get('href', ''))

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
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    sandra = sandraScraper()
    sandra.get_response()
    sandra.scrape_jobs()
    sandra.send_to_viitor()
