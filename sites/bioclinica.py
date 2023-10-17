#
#
#
# bioclinica > https://bioclinica.ro/compania/cariere

from sites.website_scraper_bs4 import BS4Scraper

class bioclinicaScraper(BS4Scraper):
    
    """
    A class for scraping job data from bioclinica website.
    """
    url = 'https://bioclinica.ro/compania/cariere'
    url_logo = 'https://bioclinica.ro/images/facebook-image.jpg'
    company_name = 'bioclinica'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from bioclinica website.
        """
        job_titles_elements = self.get_jobs_elements('css_', 'div.col-lg-7.col-md-6.col-sm-8 > a')
        job_cities_elements = self.get_jobs_elements('class_', 'text-15 text-dark-blue')
        job_url_elements = self.get_jobs_elements('class_', 'btn btn-primary text-uppercase w-100')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)
        
            
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
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    bioclinica = bioclinicaScraper()
    bioclinica.get_response()
    bioclinica.scrape_jobs()
    bioclinica.sent_to_future()