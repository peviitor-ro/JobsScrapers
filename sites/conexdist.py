#
#
#
# conexdist > https://www.conexdist.ro/ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class conexdistScrapper(BS4Scraper):
    
    """
    A class for scraping job data from conexdist website.
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
        Scrape job data from conexdist website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div > h3')
        job_cities_elements = self.get_jobs_elements('css_', 'div > p > strong')
        # job_urls_elements = self.get_jobs_elements('class_', 'button primary is-outline is-small lowercase')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)[1:-1]
        self.job_cities = self.get_jobs_details_text(job_cities_elements)[:-1]
        # self.job_urls = self.get_jobs_details_href(job_urls_elements)

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
            job_city = job_city.replace("–", "").replace("Sediul Central", "").replace("(Jilava)", "").replace("  ", " ").replace(" Iași", "Iași").split()
            self.create_jobs_dict(job_title, "https://www.conexdist.ro/ro/cariere/aplica/", "România", job_city)

if __name__ == "__main__":
    URL = 'https://www.conexdist.ro/ro/cariere/'
    URL_LOGO = 'https://www.conexdist.ro/wp-content/uploads/2020/11/Asset-2.png'
    company_name = 'conexdist'
    conexdist = conexdistScrapper(company_name, URL, URL_LOGO)
    conexdist.get_response()
    conexdist.scrape_jobs()
    conexdist.sent_to_future()
    
    

