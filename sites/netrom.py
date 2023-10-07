#
#
#
#
## Netrom > https://www.netromsoftware.ro/jobs

from sites.website_scraper_bs4 import BS4Scraper

class NetromScraper(BS4Scraper):
    
    """
    A class for scraping job data from Netrom website.
    """
    url = 'https://www.netromsoftware.ro/jobs'
    url_logo = 'https://www.icelakecapital.com/wp-content/uploads/2019/01/netrom-logo-clean.png'
    company_name = 'Netrom'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Netrom website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div.left-column.simple-page > div > ul > li > a')
        job_urls_elements = self.get_jobs_elements('css_', "div.left-column.simple-page > div > ul > li > a")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements[1:])
        self.job_urls = self.get_jobs_details_href(job_urls_elements[1:])

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
            self.create_jobs_dict(job_title, job_url, "România", "Craiova")

if __name__ == "__main__":
    Netrom = NetromScraper()
    Netrom.get_response()
    Netrom.scrape_jobs()
    Netrom.sent_to_future()
    
    

