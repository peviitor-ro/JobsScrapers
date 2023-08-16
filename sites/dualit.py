#
#
#
# dualit > https://dualit.ro/careers/

from website_scraper_bs4 import BS4Scraper

class dualitScrapper(BS4Scraper):
    
    """
    A class for scraping job data from dualit website.
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
        Scrape job data from dualit website.
        """

        job_elements = self.get_jobs_elements('css_', "a[href^='https://dualit.ro/careers/'][class='fusion-background-highlight']")
        
        self.job_titles = self.get_jobs_details_text(job_elements[1:])
        self.job_urls = self.get_jobs_details_href(job_elements[1:])

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
            self.create_jobs_dict(job_title, job_url, "Romania", "Cluj-Napoca")

if __name__ == "__main__":
    URL = 'https://dualit.ro/careers/'
    URL_LOGO = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/dualit.jpg'
    company_name = 'dualit'
    dualit = dualitScrapper(company_name, URL, URL_LOGO)
    dualit.get_response()
    dualit.scrape_jobs()
    dualit.send_to_viitor()
    
    

