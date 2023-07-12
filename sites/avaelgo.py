#
#
#
# avaelgo > https://avaelgo.ro/jobs/

from sites.website_scraper_bs4 import BS4Scraper

class avaelgoScrapper(BS4Scraper):
    
    """
    A class for scraping job data from avaelgo website.
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
        Scrape job data from avaelgo website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'article > header > h3 > a')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_titles_elements)

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
            self.create_jobs_dict(job_title, job_url, "România", "Timisoara")

if __name__ == "__main__":
    URL = 'https://avaelgo.ro/jobs/'
    URL_LOGO = 'https://avaelgo.ro/wp-content/uploads/2016/06/Avaelgo-Logo-transparent-e1490711911466.png'
    company_name = 'avaelgo'
    avaelgo = avaelgoScrapper(company_name, URL, URL_LOGO)
    avaelgo.get_response()
    avaelgo.scrape_jobs()
    avaelgo.sent_to_future()
    
    

