#
#
#
# mennekes > https://www.mennekes.ro/ro/cariera/

from sites.website_scraper_bs4 import BS4Scraper

class mennekesScraper(BS4Scraper):
    
    """
    A class for scraping job data from mennekes website.
    """
    url = 'https://recruitingapp-5150.de.umantis.com/Jobs/1?lang=eng&DesignID=10005&searchTokens=403&ContentOnly'
    url_logo = 'https://www.mennekes.ro/typo3conf/ext/twt_customer/Resources/Public/Images/logo.svg'
    company_name = 'mennekes'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from mennekes website.
        """

        job_elements = self.get_jobs_elements('class_', "HSTableLinkSubTitle")
        
        self.job_titles = self.get_jobs_details_text(job_elements)[:-1]
        self.job_urls = self.get_jobs_details_href(job_elements)[:-1]

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
            job_url = f"https://recruitingapp-5150.de.umantis.com{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    mennekes = mennekesScraper()
    mennekes.get_response()
    mennekes.scrape_jobs()
    mennekes.sent_to_future()
    
    

