#
#
#
# edutrust > https://www.edutrust.ro/cariera/#open-positions

from sites.website_scraper_bs4 import BS4Scraper

class edutrustScrapper(BS4Scraper):
    
    """
    A class for scraping job data from edutrust website.
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
        Scrape job data from edutrust website.
        """

        job_titles_elements = self.get_jobs_elements('css_', '#open-positions > div > div > div > div.uk-panel.uk-text-lead.uk-margin.uk-width-xlarge.uk-margin-auto.uk-text-center > p')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)

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
            self.create_jobs_dict(job_title[3:], self.url, "Romania", "Oradea")

if __name__ == "__main__":
    URL = 'https://www.edutrust.ro/cariera/#open-positions'
    URL_LOGO = 'https://www.edutrust.ro/wp-content/themes/yootheme/cache/39/logo-edutrust-39288933.webp'
    company_name = 'edutrust'
    edutrust = edutrustScrapper(company_name, URL, URL_LOGO)
    edutrust.get_response()
    edutrust.scrape_jobs()
    edutrust.sent_to_future()
    
    

