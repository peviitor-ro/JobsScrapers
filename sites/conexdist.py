#
#
#
# conexdist > https://www.conexdist.ro/ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class conexdistScraper(BS4Scraper):
    
    """
    A class for scraping job data from conexdist website.
    """
    url = 'https://www.conexdist.ro/ro/cariere/'
    url_logo = 'https://www.conexdist.ro/wp-content/uploads/2020/11/Asset-2.png'
    company_name = 'conexdist'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from conexdist website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div > h3')
        job_cities_elements = self.get_jobs_elements('css_', 'div > p > strong')
        job_urls_elements = self.get_jobs_elements('class_', 'button primary is-small lowercase')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)[1:-1]
        self.job_cities = self.get_jobs_details_text(job_cities_elements)[:-1]
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

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
            job_city = job_city.replace("–", "").replace("Sediul Central", "").replace(" (Jilava)", "").replace("  ", " ").replace(" Iași", "Iași").replace(",Iași", ", Iași").replace(" (Voluntari și Militari)", "").replace("Cluj", "Cluj-Napoca").split(", ")
            job_url = f"https://www.conexdist.ro{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    conexdist = conexdistScraper()
    conexdist.get_response()
    conexdist.scrape_jobs()
    conexdist.sent_to_future()
    
    

