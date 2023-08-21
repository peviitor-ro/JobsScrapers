#
#
#
# Nolimits > https://www.nolimits.ro/cariere.html

from sites.website_scraper_bs4 import BS4Scraper

class NolimitsScrapper(BS4Scraper):
    
    """
    A class for scraping job data from Nolimits website.
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
        Scrape job data from Nolimits website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div.entry-content > h1')
        
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
            self.create_jobs_dict(job_title, self.url, "România", "Satu Mare")

if __name__ == "__main__":
    URL = 'https://www.nolimits.ro/cariere.html'
    URL_LOGO = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/nolimits.PNG'
    company_name = 'Nolimits'
    Nolimits = NolimitsScrapper(company_name, URL, URL_LOGO)
    Nolimits.get_response()
    Nolimits.scrape_jobs()
    Nolimits.sent_to_future()
    
    

