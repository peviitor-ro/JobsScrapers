#
#
#
# nokia > https://careers.nokia.com/ajax/content/job_results

import requests
from sites.website_scraper_api import WebsiteScraperAPI
import subprocess

class nokiaScrape(WebsiteScraperAPI):
    
    """
    A class for scraping job data from nokia website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(company_name, url, company_logo_url)
        
    
    def set_headers(self):
        self.headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://careers.nokia.com/jobs/search/39325305',
        'tss-token': 'HZlgnlrLqWDc1YipgHq3kjs4hK6aK24GxivyinAF1zw=',
        }
        
    def set_params(self, page_index): 
        self.params = {
        'JobSearch.id': '39325305',
        'page_index': page_index,
        'site-name': 'default1784',
        'include_site': 'true',
        'uid': '289',
        }
    
    def set_cookies(self):
        self.cookies = {
        'ORA_OTSS_SESSION_ID': 'fd6e440660b66b8a42ce652a44ef4c2cb934a0c3927b163c191c5aa1252a49ca.aluperf.frprapq11308.tee.taleocloud.net'
        }
        
    def post_response(self):
        """
        Send a post request and retrieve the jobs response.
        """
        self.job_details = []
        current_page = 1
        self.set_params(current_page)
        
        """
        This chunk of code itterate over the response html from the api response and gets the url from each job
        """
        response = requests.post('https://careers.nokia.com/ajax/content/job_results', params=self.params, cookies=self.cookies, headers=self.headers)
        while response.status_code == 200:
            for res in response.text.split():
                if "https://careers.nokia.com/jobs/" in res:
                    self.job_details.append(res[7:-2])
            current_page += 1
            self.set_params(current_page)
            response = requests.post('https://careers.nokia.com/ajax/content/job_results', params=self.params, cookies=self.cookies, headers=self.headers)
        
    
    def _get_city(self, urls):
        cities = []
        
        for url in urls:
            command = ["curl", url]

            # Execute the curl command and capture the output
            output = subprocess.check_output(command)

            # Decode the output as a string
            output = output.decode("utf-8").split()
            # print(output)

            city = None

            for str_count in range(len(output)):
                if "Romania," in output[str_count]:
                    city = output[str_count-1][:-1]
            
            if city == None:
                cities.append("Bucharest")
            else:
                cities.append(city)
        
        return cities


    def scrape_jobs(self):
        """
        Scrape job data from nokia website.
        """
        # Get titles
        self.job_titles = []
        for job_detail in self.job_details:
            job_title = job_detail.replace("https://careers.nokia.com/jobs/", "").split("-")[:-1]
            self.job_titles.append(" ".join(job_title))
            

        # Get cities
        self.job_cities = self._get_city(self.job_details)
        # print(self.job_cities)
        
        # Get url ids
        self.job_urls = self.job_details
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
            self.create_jobs_dict(job_title, job_url, "România", job_city)
        

if __name__ == "__main__":
    URL = 'https://careers.nokia.com/ajax/content/job_results'
    URL_LOGO = 'https://www.nokia.com/themes/custom/onenokia_reskin/logo.svg'
    company_name = 'nokia'
    nokia = nokiaScrape(company_name, URL, URL_LOGO)
    nokia.set_headers()
    nokia.set_cookies()
    nokia.post_response()
    nokia.scrape_jobs()
    nokia.send_to_viitor()