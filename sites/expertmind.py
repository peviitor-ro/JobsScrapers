#
#
#
# expertmind > https://www.expertmind.ro/companie/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class expertmindScrapper(BS4Scraper):
    
    """
    A class for scraping job data from expertmind website.
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
        Scrape job data from expertmind website.
        """

        job_elements = self.get_jobs_elements('class_', "vc_gitem-link")
        
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
            self.create_jobs_dict(job_title, job_url, "România", ['Iasi', 'Bucuresti'])

if __name__ == "__main__":
    URL = 'https://www.expertmind.ro/companie/cariere/'
    URL_LOGO = 'https://www.expertmind.ro/wp-content/uploads/2022/06/LOGO-Expert-Mind-actualizat.jpeg'
    company_name = 'expertmind'
    expertmind = expertmindScrapper(company_name, URL, URL_LOGO)
    expertmind.get_response()
    expertmind.scrape_jobs()
    expertmind.sent_to_future()
    
    

