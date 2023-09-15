#
#
#
# polipolmobila > https://www.polipolmobila.ro/locuri-de-munca-disponibile/


from sites.website_scraper_bs4 import BS4Scraper

class polipolmobilaScraper(BS4Scraper):
    
    """
    A class for scraping job data from polipolmobila website.
    """
    url = 'https://www.polipolmobila.ro/locuri-de-munca-disponibile/'
    url_logo = 'https://www.polipolmobila.ro/media/images/web/logo.png'
    company_name = 'polipolmobila'
    
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
        Scrape job data from polipolmobila website.
        """

        job_elements = self.get_jobs_elements('css_', "td:nth-child(1)")
        
        self.job_titles = self.get_jobs_details_text(job_elements)

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
            self.create_jobs_dict(job_title, job_url, "România", "Satu Mare")
            self.job_count += 1

if __name__ == "__main__":
    polipolmobila = polipolmobilaScraper()
    polipolmobila.get_response()
    polipolmobila.scrape_jobs()
    polipolmobila.sent_to_future()
    
    

