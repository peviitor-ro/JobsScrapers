#
#
#
# canopy > https://canopy.ro/online-marketing-jobs/

from sites.website_scraper_bs4 import BS4Scraper

class canopyScraper(BS4Scraper):
    
    """
    A class for scraping job data from canopy website.
    """
    url = 'https://canopy.ro/online-marketing-jobs/'
    url_logo = 'https://canopy.ro/wp-content/uploads/2021/01/logo_principal_pozitiv-01-1.png'
    company_name = 'canopy'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from canopy website.
        """
        self.job_titles = ['Marketing Jobs - Canopy']
        self.job_urls = [self.url]
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
            self.create_jobs_dict(job_title, job_url, "România", ['Bucuresti', 'Iasi', 'Cluj-Napoca'])

if __name__ == "__main__":
    canopy = canopyScraper()
    canopy.get_response()
    canopy.scrape_jobs()
    canopy.sent_to_future()
    
    

