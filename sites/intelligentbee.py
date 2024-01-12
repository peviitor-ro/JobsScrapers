#
#
#
# intelligentbee > https://intelligentbee.com/careers-ib

from sites.website_scraper_bs4 import BS4Scraper

class intelligentbeeScraper(BS4Scraper):
    
    """
    A class for scraping job data from intelligentbee website.
    """
    url = 'https://intelligentbee.com/careers-ib'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/intelligentbee.PNG'
    company_name = 'intelligentbee'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from intelligentbee website.
        """

        job_titles_elements = self.get_jobs_elements('css_', 'div > div:nth-child(2) > div > div > div > h5')
        job_url_elements = self.get_jobs_elements('class_', 'white-btn')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
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
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            job_url = "https://intelligentbee.com" + job_url
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    intelligentbee = intelligentbeeScraper()
    intelligentbee.get_response()
    intelligentbee.scrape_jobs()
    intelligentbee.sent_to_future()
    
    

