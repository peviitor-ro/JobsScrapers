#
#
#
# aeroportoradea > https://www.aeroportoradea.ro/ro/locuri-de-munca-vacante.html


from sites.website_scraper_bs4 import BS4Scraper

class aeroportoradeaScrapper(BS4Scraper):
    
    """
    A class for scraping job data from aeroportoradea website.
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
        Scrape job data from aeroportoradea website.
        """

        job_title_elements = self.get_jobs_elements('css_', "#article-101 > div > h3")
        job_url_elements = self.get_jobs_elements('css_', "#article-101 > div > div > span > a")
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls[::3]):
            job_url = "https://www.aeroportoradea.ro" + job_url.replace(" ", "%20")
            self.create_jobs_dict(job_title.split("-")[0], job_url, "România", "Oradea")

if __name__ == "__main__":
    URL = 'https://www.aeroportoradea.ro/ro/locuri-de-munca-vacante.html'
    URL_LOGO = 'https://www.aeroportoradea.ro/images/misc/logo-2021-01.svg'
    company_name = 'aeroportoradea'
    aeroportoradea = aeroportoradeaScrapper(company_name, URL, URL_LOGO)
    aeroportoradea.get_response()
    aeroportoradea.scrape_jobs()
    aeroportoradea.sent_to_future()
    
    

