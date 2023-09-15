#
#
#
# CSGroup > https://www.c-s.ro/careers/jobs/

from sites.website_scraper_bs4 import BS4Scraper

class CSGroupScraper(BS4Scraper):
    
    """
    A class for scraping job data from CSGroup website.
    """
    url = 'https://www.c-s.ro/careers/jobs/'
    url_logo = 'https://www.c-s.ro/wp-content/uploads/2018/04/cropped-CS-Group-ROMANIA-227x103.png'
    company_name = 'CSGroup'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from CSGroup website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div.wpsm_service-content > a > h3')
        job_urls_elements = self.get_jobs_elements('class_', "wpsm_read")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
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
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Craiova")

if __name__ == "__main__":
    CSGroup = CSGroupScraper()
    CSGroup.get_response()
    CSGroup.scrape_jobs()
    CSGroup.sent_to_future()
    
    

