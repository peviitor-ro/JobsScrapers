#
#
#
# BitSoftware > https://www.bitsoftware.eu/cariere-la-bitsoftware-solutii-software-de-business-erp-crm-bi-wms/

from sites.website_scraper_bs4 import BS4Scraper

class BitSoftwareScraper(BS4Scraper):
    
    """
    A class for scraping job data from BitSoftware website.
    """
    url = 'https://www.bitsoftware.eu/cariere-la-bitsoftware-solutii-software-de-business-erp-crm-bi-wms/'
    url_logo = 'https://www.bitsoftware.eu/wp-content/uploads/BITSoftware-Entersoft-e1654160058138.png'
    company_name = 'BitSoftware'
    
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
        Scrape job data from BitSoftware website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'lsow-tab-label')
        job_urls_elements = self.get_jobs_elements('class_', "lsow-tab-label")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

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
        # Jobs that are both in brasov and bucharest because they are not structured
        job_exceptions = ['Channel Manager']
        
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            if job_title in job_exceptions:
                job_city = ['Brasov', 'Bucuresti']
            else:
                job_city = 'Bucuresti'
            job_url = f"{self.url}{job_url}#{self.job_count}"
            self.create_jobs_dict(job_title, job_url, "România", job_city)
            self.job_count += 1

if __name__ == "__main__":
    BitSoftware = BitSoftwareScraper()
    BitSoftware.get_response()
    BitSoftware.scrape_jobs()
    BitSoftware.sent_to_future()
    
    

