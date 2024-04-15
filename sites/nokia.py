#
#
#
# nokia > https://careers.nokia.com/jobs/search/40601155

import requests
from sites.website_scraper_api import WebsiteScraperAPI

class nokiaScraper(WebsiteScraperAPI):
    
    """
    A class for scraping job data from nokia website.
    """
    url = 'https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true&expand=requisitionList.secondaryLocations,flexFieldsFacet.values&finder=findReqs;siteNumber=CX_1,facetsList=LOCATIONS%3BWORK_LOCATIONS%3BWORKPLACE_TYPES%3BTITLES%3BCATEGORIES%3BORGANIZATIONS%3BPOSTING_DATES%3BFLEX_FIELDS,limit=1000,locationId=300000000471997,sortBy=POSTING_DATES_DESC'
    url_logo = 'https://www.nokia.com/themes/custom/onenokia_reskin/logo.svg'
    company_name = 'nokia'
    
    def __init__(self):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(self.company_name, self.url, self.url_logo)
        
    
    def set_headers(self):
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_8_8; like Mac OS X) AppleWebKit/535.14 (KHTML, like Gecko) Chrome/49.0.3028.253 Mobile Safari/603.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Refer': 'https://google.com',
        'DNT': '1'
        }
        
    def post_response(self):
        """
        Send a post request and retrieve the jobs response.
        """
        self.job_details = requests.get(
            self.url,
            headers=self.headers).json()['items'][0]['requisitionList']
        self.get_jobs_response(self.job_details)

    def scrape_jobs(self):
        """
        Scrape job data from nokia website.
        """
        dummy_job_url = "https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/558/?location=Romania&locationId=300000000471997&locationLevel=country&mode=location&sortBy=POSTING_DATES_DESC"
        self.job_titles = self.get_job_details(['Title'])
        self.job_ids = self.get_job_details(['Id'])
        self.job_urls = []
        for job_id in self.job_ids:
            self.job_urls.append(dummy_job_url.replace("558", job_id))
        
        self.format_data()
            
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.set_headers()
        self.post_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Timisoara")
        

if __name__ == "__main__":
    nokia = nokiaScraper()
    nokia.set_headers()
    nokia.post_response()
    nokia.scrape_jobs()
    nokia.send_to_viitor()