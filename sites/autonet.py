#
#
#
# autonet > https://www.autonet-group.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class autonetScraper(BS4Scraper):
    
    """
    A class for scraping job data from autonet website.
    """
    url = 'https://www.autonet-group.ro/cariere/'
    url_logo = 'https://www.autonet-group.ro/pub/images/logo.svg'
    company_name = 'autonet'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from autonet website.
        """

        job_title_elements = self.get_jobs_elements('class_', "fw-bolder fs-5 mb-3 text-center text-sm-start")
        job_cities_elements = self.get_jobs_elements('class_', "fs-8 mb-2 text-center text-sm-start")
        job_url_elements = self.get_jobs_elements('class_', "orange fw-bolder")
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)
        
        # while len(self.job_cities) != len(self.job_titles):
        #     self.job_cities.append("Romania")

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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = f"https://www.autonet-group.ro/{job_url}"
            if job_city == "Posturi disponibile":
                job_city = "Romania"
                
            job_city = job_city.replace("Cluj Napoca", "Cluj-Napoca").replace("Posturi disponibile - ", "").replace("sector", "").replace(" (Turda)", "").replace("3,", "").replace("4,", "").replace("-", "").replace("  ", " ").replace("Posturi disponibile", "").replace("  ", " ").split(", ")
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    autonet = autonetScraper()
    autonet.get_response()
    autonet.scrape_jobs()
    autonet.sent_to_future()
    
    

