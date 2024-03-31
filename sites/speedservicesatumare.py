#
#
#
# speedservicesatumare > https://speedservicesatumare.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class speedservicesatumareScraper(BS4Scraper):
    
    """
    A class for scraping job data from speedservicesatumare website.
    """
    url = 'https://speedservicesatumare.ro/cariere/'
    url_logo = 'https://speedservicesatumare.ro/wp-content/uploads/2018/03/logo-speed-service-satu-mare.png'
    company_name = 'speedservicesatumare'
    
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
        Scrape job data from speedservicesatumare website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div > div > div > div > h2')[:-1]

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
            self.create_jobs_dict(job_title, job_url, "România", "Satu Mare")
            self.job_count += 1

if __name__ == "__main__":
    speedservicesatumare = speedservicesatumareScraper()
    speedservicesatumare.get_response()
    speedservicesatumare.scrape_jobs()
    speedservicesatumare.sent_to_future()
    
    

