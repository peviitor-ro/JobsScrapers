#
#
#
# nokia > https://careers.nokia.com/jobs/search/40601155

import requests
from sites.website_scraper_api import WebsiteScraperAPI
import subprocess

class nokiaScraper(WebsiteScraperAPI):
    
    """
    A class for scraping job data from nokia website.
    """
    url = 'https://careers.nokia.com/ajax/content/job_results'
    url_logo = 'https://www.nokia.com/themes/custom/onenokia_reskin/logo.svg'
    company_name = 'nokia'
    
    def __init__(self):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(self.company_name, self.url, self.url_logo)
        
    
    def set_headers(self):
        self.headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://careers.nokia.com/jobs/search/40601155',
        'tss-token': 'bC9QdKulsUsqxUxRAjywuSS6iqoVfCHhb0Fy0hbJcm8=',
        }
        
    def set_params(self, page_index): 
        self.params = {
        'JobSearch.id': '40601155',
        'page_index': page_index,
        'site-name': 'default1784',
        'include_site': 'true',
        'uid': '857',
        }
    
    def set_cookies(self):
        self.cookies = {
        'ORA_OTSS_SESSION_ID': '7b05bca5b1e7a3ca264ec7d36b440c38b8d06f5dd00adf823f4b5ff82bbac101.aluperf.frprapq11308.tee.taleocloud.net'
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
          

    # Get the title data from mc until the tel item in the list
    def _get_title(self, lst):

        in_title_section = False
        results = []

        for item in lst:
            if item.startswith('class="title"'):
                in_title_section = True
                temp_list = []
            elif item.startswith("</h1>") and in_title_section:
                in_title_section = False
                results.append(" ".join(temp_list))
            elif in_title_section:
                temp_list.append(item)
            
        return results[0]
    
    def _get_data(self, urls):
        cities = []
        
        for url in urls:
            command = ["curl", url]

            # Execute the curl command and capture the output
            output = subprocess.check_output(command)

            # Decode the output as a string
            output = output.decode("utf-8").split()
            self.job_titles.append(self._get_title(output))

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
            

        # Get cities
        self.job_cities = self._get_data(self.job_details)
        # print(self.job_cities)
        
        # Get url ids
        self.job_urls = self.job_details
        self.format_data()

    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.set_headers()
        self.set_cookies()
        self.post_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)
        

if __name__ == "__main__":
    nokia = nokiaScraper()
    nokia.set_headers()
    nokia.set_cookies()
    nokia.post_response()
    nokia.scrape_jobs()
    nokia.send_to_viitor()