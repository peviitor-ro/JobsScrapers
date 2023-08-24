#
#
#
# GazduireJocuri > https://www.gazduirejocuri.ro/cariere/

from website_scraper_bs4 import BS4Scraper

class GazduireJocuriScrapper(BS4Scraper):
    
    """
    A class for scraping job data from GazduireJocuri website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        self.job_count = 1
        super().__init__(company_name, company_logo_url)
        
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
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city in zip(self.job_titles, self.job_cities):
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "Romania", job_city)
            self.job_count += 1

if __name__ == "__main__":
    URL = 'https://www.gazduirejocuri.ro/cariere/'
    URL_LOGO = 'https://www.gazduirejocuri.ro/img/logo-orange.svg'
    company_name = 'GazduireJocuri'
    GazduireJocuri = GazduireJocuriScrapper(company_name, URL, URL_LOGO)
    GazduireJocuri.get_response()
    GazduireJocuri.scrape_jobs()
    GazduireJocuri.sent_to_future()
    
    

