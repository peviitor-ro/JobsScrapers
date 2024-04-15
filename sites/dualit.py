#
#
#
# dualit > https://dualitsoft.com/careers/

from sites.website_scraper_bs4 import BS4Scraper

class dualitScraper(BS4Scraper):
    
    """
    A class for scraping job data from dualit website.
    """
    url = 'https://dualitsoft.com/careers/'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/dualit.jpg'
    company_name = 'dualit'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from dualit website.
        """

        job_elements = self.get_jobs_elements('class_', "fusion-column-anchor")
        
        self.job_urls = self.get_jobs_details_href(job_elements)
        self.job_titles = [job_title.replace("https://dualitsoft.com/careers/", "").replace("-", " ").replace("/", "").replace("ui ux", "ui/ux").title() for job_title in self.job_urls]

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
            self.create_jobs_dict(job_title.replace("Java Developer 2", "Java Developer"), job_url, "România", "Cluj-Napoca", "remote")

if __name__ == "__main__":
    dualit = dualitScraper()
    dualit.get_response()
    dualit.scrape_jobs()
    dualit.sent_to_future()
    
    

