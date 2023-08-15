#
#
#
# polipolmobila > https://www.polipolmobila.ro/locuri-de-munca-disponibile/


from sites.website_scraper_bs4 import BS4Scraper

class polipolmobilaScrapper(BS4Scraper):
    
    """
    A class for scraping job data from polipolmobila website.
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
        Scrape job data from polipolmobila website.
        """

        job_elements = self.get_jobs_elements('css_', "td:nth-child(1)")
        
        self.job_titles = self.get_jobs_details_text(job_elements)

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
            self.create_jobs_dict(job_title, "https://www.polipolmobila.ro/aplicare-online/", "România", "Satu Mare")

if __name__ == "__main__":
    URL = 'https://www.polipolmobila.ro/locuri-de-munca-disponibile/'
    URL_LOGO = 'https://www.polipolmobila.ro/media/images/web/logo.png'
    company_name = 'polipolmobila'
    polipolmobila = polipolmobilaScrapper(company_name, URL, URL_LOGO)
    polipolmobila.get_response()
    polipolmobila.scrape_jobs()
    polipolmobila.sent_to_future()
    
    

