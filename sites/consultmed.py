#
#
#
# consultmed > https://consultmed.ro/consultmed-clinica-diabet-nutritie-iasi/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class consultmedScraper(BS4Scraper):
    
    """
    A class for scraping job data from consultmed website.
    """
    url = 'https://consultmed.ro/consultmed-clinica-diabet-nutritie-iasi/cariere/'
    url_logo = 'https://consultmed.ro/wp-content/uploads/2021/06/logo7.png'
    company_name = 'consultmed'
    
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
        Scrape job data from consultmed website.
        """

        job_titles_elements = self.get_jobs_elements('css_', '#diabet > div > ul > li')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)

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
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")
            self.job_count += 1

if __name__ == "__main__":
    consultmed = consultmedScraper()
    consultmed.get_response()
    consultmed.scrape_jobs()
    consultmed.sent_to_future()
    
    

