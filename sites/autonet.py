#
#
#
# autonet > https://www.autonet-group.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class autonetScrapper(BS4Scraper):
    
    """
    A class for scraping job data from autonet website.
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
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = f"https://www.autonet-group.ro/{job_url}"
            if job_city == "Posturi disponibile":
                job_city = "Romania"
                
            # print(job_city.replace("Posturi disponibile - ", "").replace("sector", "").replace("3,", "").replace("4,", "").replace("-", "").replace("  ", " ").replace("Posturi disponibile", "").replace("  ", " ").split())
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace("Posturi disponibile - ", "").replace("sector", "").replace("3,", "").replace("4,", "").replace("-", "").replace("  ", "").replace("Posturi disponibile", "").replace("  ", " ").split())

if __name__ == "__main__":
    URL = 'https://www.autonet-group.ro/cariere/'
    URL_LOGO = 'https://www.autonet-group.ro/pub/images/logo.svg'
    company_name = 'autonet'
    autonet = autonetScrapper(company_name, URL, URL_LOGO)
    autonet.get_response()
    autonet.scrape_jobs()
    autonet.sent_to_future()
    
    

