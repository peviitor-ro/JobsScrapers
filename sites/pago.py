#
#
#
# Pago > https://pago.ro/#section-13


from sites.website_scraper_bs4 import BS4Scraper

class PagoScrapper(BS4Scraper):
    
    """
    A class for scraping job data from Pago website.
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
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            job_url = f"https://pago.ro/{job_url}"
            if job_title and job_city and job_url:
                self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://pago.ro/#section-13'
    URL_LOGO = 'https://besticon-demo.herokuapp.com/lettericons/P-120-6a4397.png'
    company_name = 'Pago'
    Pago = PagoScrapper(company_name, URL, URL_LOGO)
    Pago.get_response()
    Pago.scrape_jobs()
    Pago.sent_to_future()
    
    

