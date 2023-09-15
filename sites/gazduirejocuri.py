#
#
#
# GazduireJocuri > https://www.gazduirejocuri.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class GazduireJocuriScraper(BS4Scraper):
    
    """
    A class for scraping job data from GazduireJocuri website.
    """
    url = 'https://www.gazduirejocuri.ro/cariere/'
    url_logo = 'https://www.gazduirejocuri.ro/img/logo-orange.svg'
    company_name = 'GazduireJocuri'
    
    
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
        Scrape job data from GazduireJocuri website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'section-heading f-28')
        job_cities_elements = self.get_jobs_elements('css_', 'li:nth-child(2) > b')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)
        # IN ACEST CAZ TOATE JOBURILE DUC LA PAGINA DE CONTACT
        # TOATE JOBURILE CARE SE POSTEAZA SUNT DIN ROMANIA
        
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
        for job_title, job_city in zip(self.job_titles, self.job_cities):
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", job_city)
            self.job_count += 1

if __name__ == "__main__":
    GazduireJocuri = GazduireJocuriScraper()
    GazduireJocuri.get_response()
    GazduireJocuri.scrape_jobs()
    GazduireJocuri.sent_to_future()
    
    

