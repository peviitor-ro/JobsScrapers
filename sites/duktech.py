#
# 
#
# duktech > https://www.duk-tech.com/


from website_scraper_bs4 import BS4Scraper

class duktechScrapper(BS4Scraper):
    
    """
    A class for scraping job data from duktech website.
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
        Scrape job data from duktech website.
        """

        job_elements = self.get_jobs_elements('css_', 'div.flex-column.d-flex.col-md-3.col-6 > span > a')
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)
        
        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            job_url = f"https://www.duk-tech.com{job_url}"
            self.create_jobs_dict(job_title, job_url, "Romania", "Iasi")

if __name__ == "__main__":
    URL = 'https://www.duk-tech.com/'
    URL_LOGO = 'https://imgcdn.bestjobs.eu/cdn/el/plain/employer_logo/5c59670789be5.png'
    company_name = 'duktech'
    duktech = duktechScrapper(company_name, URL, URL_LOGO)
    duktech.get_response()
    duktech.scrape_jobs()
    duktech.sent_to_future()
    
    

