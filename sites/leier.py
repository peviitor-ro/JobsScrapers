#
#
#
# leier > https://www.leier.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class leierScrapper(BS4Scraper):
    
    """
    A class for scraping job data from leier website.
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
        Scrape job data from leier website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "awsm-job-post-title")
        job_location_elements = self.get_jobs_elements('class_', "locatie_text")
        job_url_elements = self.get_jobs_elements('id_', 'awsm-grid-item-2440')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_location_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)

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
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://www.leier.ro/cariere/'
    URL_LOGO = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc0aKksxn_ZPQOnyn9-dAc9KQkWMPWwG5d7cuYX8AUgGV0xIuDqAFpt14Q7b5yNwqHGAk'
    company_name = 'leier'
    leier = leierScrapper(company_name, URL, URL_LOGO)
    leier.get_response()
    leier.scrape_jobs()
    leier.sent_to_future()
    
    

