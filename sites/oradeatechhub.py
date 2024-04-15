#
# 
#
# oradeatechhub > https://www.oradeatechhub.ro/jobs

from sites.website_scraper_bs4 import BS4Scraper

class oradeatechhubScraper(BS4Scraper):
    
    """
    A class for scraping job data from oradeatechhub website.
    """
    url = 'https://www.oradeatechhub.ro/jobs'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/oradeatechhub.PNG'
    company_name = 'oradeatechhub'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
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
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = f"https://www.oradeatechhub.ro{job_url}"
            if job_city == "Remote" or not job_city:
                remote = "remote"
                job_city = "Oradea"
            elif job_city == "Oradea/Remote":
                job_city = "Oradea"
                remote = "On-site"
            else:
                remote = "On-site"
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace("Romania", "Oradea").split(", "), remote)

if __name__ == "__main__":
    oradeatechhub = oradeatechhubScraper()
    oradeatechhub.get_response()
    oradeatechhub.scrape_jobs()
    oradeatechhub.sent_to_future()
    
    

