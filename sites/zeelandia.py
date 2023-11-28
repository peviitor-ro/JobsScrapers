#
#
#
# zeelandia > https://www.zeelandia.ro/cariere

from sites.website_scraper_bs4 import BS4Scraper

class zeelandiaScraper(BS4Scraper):
    
    """
    A class for scraping job data from zeelandia website.
    """
    url = 'https://www.zeelandia.ro/cariere'
    url_logo = 'https://www.zeelandia.ro/@@site-logo/zeelandia.png'
    company_name = 'zeelandia'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from zeelandia website.
        """

        job_title_elements = self.get_jobs_elements('class_', "feature-h")
        job_link_elements = self.get_jobs_elements('css_', "a[href$='.pdf']")
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_urls = self.get_jobs_details_href(job_link_elements)

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
            self.create_jobs_dict(job_title, job_url, "România", "Chiajna")

if __name__ == "__main__":
    zeelandia = zeelandiaScraper()
    zeelandia.get_response()
    zeelandia.scrape_jobs()
    zeelandia.sent_to_future()
    

