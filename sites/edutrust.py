#
#
#
# edutrust > https://www.edutrust.ro/cariera/#open-positions

from sites.website_scraper_bs4 import BS4Scraper

class edutrustScraper(BS4Scraper):
    
    """
    A class for scraping job data from edutrust website.
    """
    url = 'https://www.edutrust.ro/cariera/#open-positions'
    url_logo = 'https://www.edutrust.ro/wp-content/themes/yootheme/cache/3c/logo-edutrust-3ced61da.webp'
    company_name = 'edutrust'
    
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
        Scrape job data from edutrust website.
        """

        job_titles_elements = self.get_jobs_elements('css_', '#open-positions > div > div > div > div.uk-panel.uk-text-lead.uk-margin.uk-width-xlarge.uk-margin-auto.uk-text-center > p')
        
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
            self.create_jobs_dict(job_title[3:], job_url, "România", "Oradea")
            self.job_count += 1

if __name__ == "__main__":
    edutrust = edutrustScraper()
    edutrust.get_response()
    edutrust.scrape_jobs()
    edutrust.sent_to_future()
    
    

