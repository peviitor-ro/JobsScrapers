#
#
#
# ellisium > https://ellisium.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class ellisiumScrapper(BS4Scraper):
    
    """
    A class for scraping job data from ellisium website.
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
        Scrape job data from ellisium website.
        """

        job_elements = self.get_jobs_elements('css_', 'div.elementor-element.elementor-element-1b4a7cf.elementor-widget.elementor-widget-text-editor > div > div > div > p > strong')
        
        self.job_titles = self.get_jobs_details_text(job_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")
            self.job_count += 1

if __name__ == "__main__":
    URL = 'https://ellisium.ro/cariere/'
    URL_LOGO = 'https://ellisium.ro/wp-content/uploads/2022/08/Ellisium-vertical@4x-2048x1441.png.webp'
    company_name = 'ellisium'
    ellisium = ellisiumScrapper(company_name, URL, URL_LOGO)
    ellisium.get_response()
    ellisium.scrape_jobs()
    ellisium.sent_to_future()
    
    

