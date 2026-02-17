#
#
#
# anahr > https://anahr.ro/domenii/joburi-pe-domenii/

from sites.website_scraper_api import WebsiteScraperAPI
import requests

class anahrScraper(WebsiteScraperAPI):
    
    """
    A class for scraping job data from anahr website.
    """
    url = 'https://anahr.zohorecruit.com/recruit/v2/public/Job_Openings?pagename=Careers&source=CareerSite'
    url_logo = 'https://anahr.ro/wp-content/uploads/2023/01/logo-01.svg'
    company_name = 'anahr'
    
    def __init__(self):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(self.company_name, self.url, self.url_logo)

    def set_headers(self):
        self.headers = {
            'Accept': 'application/json'
        }

    def get_response(self):
        """
        Send a GET request and retrieve the jobs response.
        """
        self.job_details = requests.get(
            self.url, headers=self.headers).json()['data']
        
        self.get_jobs_response(self.job_details)

    def scrape_jobs(self):
        """
        Scrape job data from CGM website.
        """
        self.job_titles = self.get_job_details(['Posting_Title'])
        self.job_cities = self.get_job_details(['City'])
        self.job_urls = self.get_job_details(['$url'])
        self.format_data()

    def sent_to_future(self):
        self.send_to_viitor()

    def return_data(self):
        self.set_headers()
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)


if __name__ == "__main__":
    anahr = anahrScraper()
    anahr.set_headers()
    anahr.get_response()
    anahr.scrape_jobs()
    anahr.sent_to_future()

