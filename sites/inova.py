#
#
#
# inovagroup > https://www.inova-group.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class inovagroupScrapper(BS4Scraper):
    
    """
    A class for scraping job data from inovagroup website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.website_url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.website_url)
    
    def scrape_jobs(self):
        """
        Scrape job data from inovagroup website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "vc-hoverbox-block-inner vc-hoverbox-front-inner")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        print(self.job_titles)

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
            self.create_jobs_dict(job_title, self.website_url, "România", "Oradea")

if __name__ == "__main__":
    URL = 'https://www.inova-group.ro/cariere/'
    URL_LOGO = 'https://www.inova-group.ro/wp-content/uploads/2018/01/logo-mediu-1.png'
    company_name = 'inovagroup'
    inovagroup = inovagroupScrapper(company_name, URL, URL_LOGO)
    inovagroup.get_response()
    inovagroup.scrape_jobs()
    inovagroup.sent_to_future()
    
    

