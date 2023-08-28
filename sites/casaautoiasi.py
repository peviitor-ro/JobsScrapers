#
# 
#
# casaautoiasi > https://www.casaautoiasi.ro/cariere/


from website_scraper_bs4 import BS4Scraper

class casaautoiasiScrapper(BS4Scraper):
    
    """
    A class for scraping job data from casaautoiasi website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        self.job_count = 1
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from casaautoiasi website.
        """

        job_elements = self.get_jobs_elements('css_', 'p > strong')
        
        self.job_titles = self.get_jobs_details_text(job_elements)[2::4]
        
        self.format_data()

    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")
            self.job_count += 1

if __name__ == "__main__":
    URL = 'https://www.casaautoiasi.ro/cariere/'
    URL_LOGO = 'https://www.casaautoiasi.ro/wp-content/themes/theme50604/images/logo.png'
    company_name = 'casaautoiasi'
    casaautoiasi = casaautoiasiScrapper(company_name, URL, URL_LOGO)
    casaautoiasi.get_response()
    casaautoiasi.scrape_jobs()
    casaautoiasi.sent_to_future()
    
    

