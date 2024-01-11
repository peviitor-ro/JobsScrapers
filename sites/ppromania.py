#
#
#
# ppromania > https://ppromania.ro/en/career-opportunities/

from sites.website_scraper_bs4 import BS4Scraper
import subprocess
import re
import json

class ppromaniaScraper(BS4Scraper):
    
    """
    A class for scraping job data from ppromania website.
    """
    url = 'https://ppromania.ro/jm-ajax/get_listings/'
    url_logo = 'https://ppromania.ro/wp-content/uploads/2021/04/pp-Logo-web.png'
    company_name = 'ppromania'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    
    def scrape_jobs(self):
        """
        Scrape job data from ppromania website.
        """
        
        command = ["curl", self.url]

        # Execute the curl command and capture the output
        output = subprocess.check_output(command)

        # Decode the output as a string
        output = output.decode("utf-8")
        data = json.loads(output)

        # Extract text using regex :(
        self.job_titles = re.findall(r'<h3>(.*?)<\/h3>', data["html"])
        self.job_urls = re.findall(r'<a href="(.*?)">\n', data["html"])
        self.job_cities = re.findall(r'class="location">\n\t\t\t(.*?)\t\t</div>', data["html"])
        
        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            if "Remote" in job_city:
                job_city = "all"
                remote = remote
            else:
                remote = "On-site"
                
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace(" / Ilfov", "").split(), remote)

if __name__ == "__main__":
    ppromania = ppromaniaScraper()
    ppromania.scrape_jobs()
    ppromania.sent_to_future()
    
    

