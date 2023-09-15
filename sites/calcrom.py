#
# 
#
# calcrom > https://calcrom.ro/#careers


from sites.website_scraper_bs4 import BS4Scraper

class calcromScraper(BS4Scraper):
    
    """
    A class for scraping job data from calcrom website.
    """
    url = 'https://calcrom.ro/#careers'
    url_logo = 'https://calcrom.ro/wp-content/uploads/2018/11/CalCrom_Logo_82.jpg'
    company_name = 'calcrom'
    
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)
        
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
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")
            self.job_count += 1

if __name__ == "__main__":
    calcrom = calcromScraper()
    calcrom.get_response()
    calcrom.scrape_jobs()
    calcrom.sent_to_future()
    
    

