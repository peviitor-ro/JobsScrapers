#
#
#
# bbcollection > https://www.bbcollection.ro/cariera.html


from sites.website_scraper_bs4 import BS4Scraper

class bbcollectionScraper(BS4Scraper):
    
    """
    A class for scraping job data from bbcollection website.
    """
    url = 'https://www.bbcollection.ro/cariera.html'
    url_logo = 'https://www.bbcollection.ro/webroot/img/logo-bbcollection.jpg'
    company_name = 'bbcollection'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """

        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from bbcollection website.
        """

        job_title_elements = self.get_jobs_elements('css_', "a > div > h5")
        job_location_elements = self.get_jobs_elements('css_', "a > div > p:nth-child(2)")
        job_url_elements = self.get_jobs_elements('css_', 'section:nth-child(7) > div > div > div > div > div > div > a')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)
        
        job_cities = self.get_jobs_details_text(job_location_elements)
        self.job_cities = []
        
        for job_city in job_cities:
            self.job_cities.append(job_city.replace("Job disponibil in ", "").replace("Job disponibil in: ", "").split())
    

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
            job_url = f"https://www.bbcollection.ro{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    bbcollection = bbcollectionScraper()
    bbcollection.get_response()
    bbcollection.scrape_jobs()
    bbcollection.sent_to_future()
    
    

