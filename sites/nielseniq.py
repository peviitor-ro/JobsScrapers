#
# 
#
# nielseniq > https://nielseniq.com/?s=&market=global&language=en&orderby=&order=&post_type=career_job&job_locations=romania&job_teams=&job_types=


from sites.website_scraper_bs4 import BS4Scraper

class nielseniqScrapper(BS4Scraper):
    
    """
    A class for scraping job data from nielseniq website.
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
        Scrape job data from nielseniq website.
        """

        job_title_elements = self.get_jobs_elements('class_', 'entry-title')
        job_city_elements = self.get_jobs_elements('css_', 'header > div:nth-child(2) > span:nth-child(1)')
        job_url_elements = self.get_jobs_elements('class_', 'card-cover-link')
        
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
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://nielseniq.com/?s=&market=global&language=en&orderby=&order=&post_type=career_job&job_locations=romania&job_teams=&job_types='
    URL_LOGO = 'https://c.smartrecruiters.com/sr-company-images-prod-aws-dc5/5f20077aa2b8ac7a5a26cb93/c83a18a7-1926-4be1-9572-10cc0fbdc9b3/huge?r=s3-eu-central-1&_1677595339802'
    company_name = 'nielseniq'
    nielseniq = nielseniqScrapper(company_name, URL, URL_LOGO)
    nielseniq.get_response()
    nielseniq.scrape_jobs()
    nielseniq.sent_to_future()
    
    

