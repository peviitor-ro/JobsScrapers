#
#
#
# bakertilly > https://www.bakertilly.ro/careers/job-openings/

from sites.website_scraper_bs4 import BS4Scraper

class bakertillyScraper(BS4Scraper):
    
    """
    A class for scraping job data from bakertilly website.
    """
    url = 'https://www.bakertilly.ro/careers/job-openings/'
    url_logo = 'https://www.bakertilly.ro/wp-content/uploads/2019/08/BK-Logoweb.jpg'
    company_name = 'bakertilly'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from bakertilly website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "div.vc_gitem-zone.vc_gitem-zone-c > div > div > div > div > h4 > a")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_titles_elements)

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
            self.create_jobs_dict(job_title, job_url, "România", "Bucuresti")
            # if "Bucharest" in job_title:
            #     self.create_jobs_dict(job_title, job_url, "România", "Bucuresti")
            # # If there is not () in the title it means its from the default location: Bucharest otherwise is from another country
            # if "(" not in job_title and ")" not in job_title:
            #     self.create_jobs_dict(job_title, job_url, "România", "Bucuresti")

if __name__ == "__main__":
    bakertilly = bakertillyScraper()
    bakertilly.get_response()
    bakertilly.scrape_jobs()
    bakertilly.sent_to_future()
    
    

