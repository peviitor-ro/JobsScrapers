#
#
#
# velpitar > https://velpitar.ro/cariere-vel-pitar/

from sites.website_scraper_bs4 import BS4Scraper

class velpitarScraper(BS4Scraper):
    
    """
    A class for scraping job data from velpitar website.
    """
    url = 'https://velpitar.ro/cariere-vel-pitar/'
    url_logo = 'https://velpitar.ro/wp-content/uploads/2023/05/cropped-Backup_of_Sigla-Finala-fara-spate-CMYK.png'
    company_name = 'velpitar'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from velpitar website.
        """

        job_elements = self.get_jobs_elements('css_', 'h4 > a')
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)
        self.job_cities = [job_city.split("–")[-1] if "–" in job_city else job_city.split("-")[-1] for job_city in self.job_titles]
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
            self.create_jobs_dict(job_title, job_url, "România", job_city[1:].replace("Cluj", "Cluj-Napoca").split(", "))

if __name__ == "__main__":
    velpitar = velpitarScraper()
    velpitar.get_response()
    velpitar.scrape_jobs()
    velpitar.sent_to_future()
    
    

