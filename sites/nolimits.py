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
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            self.create_jobs_dict(job_title, self.url, "Romania", "Satu Mare")

if __name__ == "__main__":
    URL = 'https://www.nolimits.ro/cariere.html'
    URL_LOGO = 'https://scontent.fomr1-1.fna.fbcdn.net/v/t39.30808-6/302592411_400315428913007_1015975908567741945_n.jpg?_nc_cat=111&cb=99be929b-59f725be&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=6NFhJ1HK9hYAX-Rti9E&_nc_ht=scontent.fomr1-1.fna&oh=00_AfDpB9Xva4LL2dgBbwtw5jCMhm5Hdpxg7_7RTapkItkmGQ&oe=64BF5D48'
    company_name = 'Nolimits'
    Nolimits = NolimitsScrapper(company_name, URL, URL_LOGO)
    Nolimits.get_response()
    Nolimits.scrape_jobs()
    
    

