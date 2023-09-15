#
#
#
# avaelgo > https://avaelgo.ro/jobs/

from sites.website_scraper_bs4 import BS4Scraper

class avaelgoScraper(BS4Scraper):
    
    """
    A class for scraping job data from avaelgo website.
    """
    url = 'https://avaelgo.ro/jobs/'
    url_logo = 'https://avaelgo.ro/wp-content/uploads/2016/06/Avaelgo-Logo-transparent-e1490711911466.png'
    company_name = 'avaelgo'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from avaelgo website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'article > header > h3 > a')
        
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
            self.create_jobs_dict(job_title, job_url, "România", "Timisoara")

if __name__ == "__main__":
    avaelgo = avaelgoScraper()
    avaelgo.get_response()
    avaelgo.scrape_jobs()
    avaelgo.sent_to_future()
    
    

