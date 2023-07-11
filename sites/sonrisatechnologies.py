#
#
#
# sonrisatechnologies > https://www.careers.sonrisa.hu/#jobs

from sites.website_scraper_bs4 import BS4Scraper

class sonrisatechnologiesScrapper(BS4Scraper):
    
    """
    A class for scraping job data from sonrisatechnologies website.
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
        Scrape job data from sonrisatechnologies website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'text-block-base-link sm:min-w-[25%] sm:truncate company-link-style')
        job_urls_elements = self.get_jobs_elements('css_', "#jobs > div > ul > li > a")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)

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
            self.create_jobs_dict(job_title, job_url, "România", "Oradea")

if __name__ == "__main__":
    URL = 'https://www.careers.sonrisa.hu/#jobs'
    URL_LOGO = 'https://images.teamtailor-cdn.com/images/s3/teamtailor-production/logotype-v3/image_uploads/fc3ad244-a68c-4d8a-a08c-93eb807f80be/original.png'
    company_name = 'sonrisatechnologies'
    sonrisatechnologies = sonrisatechnologiesScrapper(company_name, URL, URL_LOGO)
    sonrisatechnologies.get_response()
    sonrisatechnologies.scrape_jobs()
    sonrisatechnologies.sent_to_future()
    
    

