#
# 
#
# calcrom > https://calcrom.ro/#careers


from website_scraper_bs4 import BS4Scraper

class calcromScrapper(BS4Scraper):
    
    """
    A class for scraping job data from calcrom website.
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
        Scrape job data from calcrom website.
        """

        job_title_elements = self.get_jobs_elements('css_', 'h3 > b')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        # self.job_urls = self.get_jobs_details_href(job_elements)
        
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
            self.create_jobs_dict(job_title, self.url, "Romania", "Iasi")

if __name__ == "__main__":
    URL = 'https://calcrom.ro/#careers'
    URL_LOGO = 'https://calcrom.ro/wp-content/uploads/2018/11/CalCrom_Logo_82.jpg'
    company_name = 'calcrom'
    calcrom = calcromScrapper(company_name, URL, URL_LOGO)
    calcrom.get_response()
    calcrom.scrape_jobs()
    calcrom.sent_to_future()
    
    

