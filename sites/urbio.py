#
#
#
# urbio > https://urbio-romania.ro/cariere/#1662454401930-ce44399a-786c

from sites.website_scraper_bs4 import BS4Scraper

class urbioScrapper(BS4Scraper):
    
    """
    A class for scraping job data from urbio website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        self.job_count = 1
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from urbio website.
        """

        job_title_elements = self.get_jobs_elements('class_', 'vc_tta-title-text')
        job_url_elements = self.get_jobs_elements('css_', 'p:nth-child(1) > b')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_cities = self.get_jobs_details_text(job_url_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city in zip(self.job_titles, self.job_cities):
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace("Romania", "").replace(", ", ""))
            self.job_count += 1

if __name__ == "__main__":
    URL = 'https://urbio-romania.ro/cariere/#1662454401930-ce44399a-786c'
    URL_LOGO = 'https://urbio-romania.ro/wp-content/uploads/2022/11/urbio-logo.svg'
    company_name = 'urbio'
    urbio = urbioScrapper(company_name, URL, URL_LOGO)
    urbio.get_response()
    urbio.scrape_jobs()
    urbio.sent_to_future()
    
    

