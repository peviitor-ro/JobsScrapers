#
#
#
# softexco > https://softexco.ro/p/cariere#aplica

from sites.website_scraper_bs4 import BS4Scraper

class softexcoScraper(BS4Scraper):
    
    """
    A class for scraping job data from softexco website.
    """
    url = 'https://softexco.ro/p/cariere'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/softexco.PNG'
    company_name = 'softexco'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from softexco website.
        """

        # Get the jobs
        job_titles_elements = self.get_jobs_elements('class_', "position")
        job_link_elements = self.get_jobs_elements('class_', "careers-button")
        
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_link_elements)

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
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            job_url = f"{self.url}{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", "Cluj-Napoca")

if __name__ == "__main__":
    softexco = softexcoScraper()
    softexco.get_response()
    softexco.scrape_jobs()
    softexco.sent_to_future()
    
    

