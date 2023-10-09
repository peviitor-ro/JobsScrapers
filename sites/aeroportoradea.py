#
#
#
# aeroportoradea > https://www.aeroportoradea.ro/ro/locuri-de-munca-vacante.html


from sites.website_scraper_bs4 import BS4Scraper

class aeroportoradeaScraper(BS4Scraper):
    
    """
    A class for scraping job data from aeroportoradea website.
    """
    url = 'https://www.aeroportoradea.ro/ro/locuri-de-munca-vacante.html'
    url_logo = 'https://www.aeroportoradea.ro/images/misc/logo-2021-01.svg'
    company_name = 'aeroportoradea'
    
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
        Scrape job data from aeroportoradea website.
        """

        job_title_elements = self.get_jobs_elements('css_', "#article-101 > div > h3")
        job_url_elements = self.get_jobs_elements('css_', "#article-101 > div > div > span > a")
        
        self.job_titles = [job_title for job_title in self.get_jobs_details_text(job_title_elements) if job_title != '']
        self.job_urls = self.get_jobs_details_href(job_url_elements)[::3]

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
            job_url = "https://www.aeroportoradea.ro" + job_url.replace(" ", "%20") + "#" + str(self.job_count)
            self.create_jobs_dict(job_title.split("-")[0], job_url, "România", "Oradea")
            self.job_count += 1

if __name__ == "__main__":
    aeroportoradea = aeroportoradeaScraper()
    aeroportoradea.get_response()
    aeroportoradea.scrape_jobs()
    aeroportoradea.sent_to_future()
    
    

