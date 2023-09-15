#
#
#
# Nolimits > https://www.nolimits.ro/cariere.html

from sites.website_scraper_bs4 import BS4Scraper

class NolimitsScraper(BS4Scraper):
    
    """
    A class for scraping job data from Nolimits website.
    """
    url = 'https://www.nolimits.ro/cariere.html'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/nolimits.PNG'
    company_name = 'Nolimits'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
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
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            self.create_jobs_dict(job_title, self.url, "România", "Satu Mare")

if __name__ == "__main__":
    Nolimits = NolimitsScraper()
    Nolimits.get_response()
    Nolimits.scrape_jobs()
    Nolimits.sent_to_future()
    
    

