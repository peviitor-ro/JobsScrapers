#
# 
#
# duktech > https://www.duk-tech.com/career


from sites.website_scraper_bs4 import BS4Scraper

class duktechScraper(BS4Scraper):
    
    """
    A class for scraping job data from duktech website.
    """
    url = 'https://www.duk-tech.com/career'
    url_logo = 'https://imgcdn.bestjobs.eu/cdn/el/plain/employer_logo/5c59670789be5.png'
    company_name = 'duktech'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from duktech website.
        """

        job_elements = self.get_jobs_elements('class_', 'card-title')
        
        titles = self.get_jobs_details_text(job_elements)
        self.job_titles = [t for t in titles if 'Manager' in t or 'Architect' in t]
        
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
            job_url = self.url
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    duktech = duktechScraper()
    duktech.get_response()
    duktech.scrape_jobs()
    duktech.sent_to_future()
    
    

