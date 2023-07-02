#
#
#
# CSGroup > https://www.c-s.ro/careers/jobs/

from website_scraper_bs4 import BS4Scraper

class CSGroupScrapper(BS4Scraper):
    
    """
    A class for scraping job data from CSGroup website.
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
        Scrape job data from CSGroup website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div.wpsm_service-content > a > h3')
        job_urls_elements = self.get_jobs_elements('class_', "wpsm_read")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

        self.format_data()
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            if job_title and job_url:
                self.create_jobs_dict(job_title, job_url, "Romania", "Craiova")

if __name__ == "__main__":
    URL = 'https://www.c-s.ro/careers/jobs/'
    URL_LOGO = 'https://www.c-s.ro/wp-content/uploads/2018/04/cropped-CS-Group-ROMANIA-227x103.png'
    company_name = 'CSGroup'
    CSGroup = CSGroupScrapper(company_name, URL, URL_LOGO)
    CSGroup.get_response()
    CSGroup.scrape_jobs()
    
    

