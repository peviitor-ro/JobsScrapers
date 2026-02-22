#
#
#
# polipolmobila > https://www.polipolmobila.ro/jobs


from sites.website_scraper_bs4 import BS4Scraper

class polipolmobilaScraper(BS4Scraper):
    
    """
    A class for scraping job data from polipolmobila website.
    """
    url = 'https://www.polipolmobila.ro/jobs'
    url_logo = 'https://www.polipolmobila.ro/logo-polipol.svg'
    company_name = 'polipolmobila'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from polipolmobila website.
        """

        job_title_elements = self.get_jobs_elements('css_', 'article h3')
        job_url_elements = self.get_jobs_elements('css_', 'article a[href^="/jobs/"]')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_urls = self.get_jobs_details_tag('href', job_url_elements)

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
            job_url = f"https://www.polipolmobila.ro{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", "Foieni")

if __name__ == "__main__":
    polipolmobila = polipolmobilaScraper()
    polipolmobila.get_response()
    polipolmobila.scrape_jobs()
    polipolmobila.sent_to_future()
    
    

