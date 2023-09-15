#
#
#
# Pago > https://pago.ro/#section-13


from sites.website_scraper_bs4 import BS4Scraper

class PagoScraper(BS4Scraper):
    
    """
    A class for scraping job data from Pago website.
    """
    url = 'https://pago.ro/#section-13'
    url_logo = 'https://besticon-demo.herokuapp.com/lettericons/P-120-6a4397.png'
    company_name = 'Pago'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Pago website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'job-name-text')
        job_urls_elements = self.get_jobs_elements('css_', "a[class='button green']")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)
        self.job_cities = []
        
        # Itterate over links get the job city only remove unwanted data
        for job_url in self.job_urls:
            self.get_content(f"https://pago.ro/{job_url}")
            job_city_element = self.get_jobs_elements('class_', 'job-site')
            self.job_cities.append(self.get_jobs_details_text(job_city_element)[0].split()[0].replace(",", ""))
        
        

        self.format_data()
        # print(self.formatted_data)
        # self.send_to_viitor()
        
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
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            job_url = f"https://pago.ro/{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    Pago = PagoScraper()
    Pago.get_response()
    Pago.scrape_jobs()
    Pago.sent_to_future()
    
    

