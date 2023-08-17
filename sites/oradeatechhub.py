#
# 
#
# oradeatechhub > https://www.oradeatechhub.ro/jobs

from sites.website_scraper_bs4 import BS4Scraper

class oradeatechhubScrapper(BS4Scraper):
    
    """
    A class for scraping job data from oradeatechhub website.
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
        Scrape job data from oradeatechhub website.
        """

        job_title_elements = self.get_jobs_elements('class_', 'heading-4')
        job_city_elements = self.get_jobs_elements('css_', 'div:nth-child(1) > div:nth-child(2) > div.location')
        job_url_elements = self.get_jobs_elements('class_', 'card-jobs w-inline-block')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_cities = self.get_jobs_details_text(job_city_elements)
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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = f"https://www.oradeatechhub.ro/{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://www.oradeatechhub.ro/jobs'
    URL_LOGO = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/oradeatechhub.PNG'
    company_name = 'oradeatechhub'
    oradeatechhub = oradeatechhubScrapper(company_name, URL, URL_LOGO)
    oradeatechhub.get_response()
    oradeatechhub.scrape_jobs()
    oradeatechhub.sent_to_future()
    
    

