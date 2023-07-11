#
#
#
# anahr > https://anahr.ro/domenii/joburi-pe-domenii/

from sites.website_scraper_bs4 import BS4Scraper

class anahrScrapper(BS4Scraper):
    
    """
    A class for scraping job data from anahr website.
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
        Scrape job data from anahr website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'uk-link-reset')
        job_urls_elements = self.get_jobs_elements('class_', "el-link uk-button uk-button-primary")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Oradea")

if __name__ == "__main__":
    URL = 'https://anahr.ro/domenii/joburi-pe-domenii/'
    URL_LOGO = 'https://anahr.ro/wp-content/uploads/2023/01/logo-01.svg'
    company_name = 'anahr'
    anahr = anahrScrapper(company_name, URL, URL_LOGO)
    anahr.get_response()
    anahr.scrape_jobs()
    anahr.sent_to_future()
    
    

