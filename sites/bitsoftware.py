#
#
#
# BitSoftware > https://www.bitsoftware.eu/cariere-la-bitsoftware-solutii-software-de-business-erp-crm-bi-wms/

from website_scraper_bs4 import BS4Scraper

class BitSoftwareScrapper(BS4Scraper):
    
    """
    A class for scraping job data from BitSoftware website.
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
        Scrape job data from BitSoftware website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'lsow-tab-label')
        job_urls_elements = self.get_jobs_elements('class_', "lsow-tab-label")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

        self.format_data()
        self.send_to_viitor()

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            job_url = f"{self.url}{job_url}"
            if job_title and job_url:
                self.create_jobs_dict(job_title, job_url, "Romania", "Bucuresti")

if __name__ == "__main__":
    URL = 'https://www.bitsoftware.eu/cariere-la-bitsoftware-solutii-software-de-business-erp-crm-bi-wms/'
    URL_LOGO = 'https://www.bitsoftware.eu/wp-content/uploads/BITSoftware-Entersoft-e1654160058138.png'
    company_name = 'BitSoftware'
    BitSoftware = BitSoftwareScrapper(company_name, URL, URL_LOGO)
    BitSoftware.get_response()
    BitSoftware.scrape_jobs()
    
    

