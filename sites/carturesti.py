#
#
#
# carturesti > https://carturesti.ro/info/joburi

from sites.website_scraper_bs4 import BS4Scraper

class carturestiScraper(BS4Scraper):
    
    """
    A class for scraping job data from carturesti website.
    """
    url = 'https://carturesti.ro/info/joburi'
    url_logo = 'https://shopniac.ro/wp-content/uploads/2016/06/logo-libraria-carturesti.jpg'
    company_name = 'carturesti'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from carturesti website.
        """

        job_title_elements = self.get_jobs_elements('css_', 'div:nth-child(7) > div > h2')
        job_location_elements = self.get_jobs_elements('css_', 'tr:nth-child(2) > td:nth-child(2)')
        job_url_elements = self.get_jobs_elements('class_', 'job-button')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_cities = self.get_jobs_details_text(job_location_elements)
        self.job_urls = self.get_jobs_details_tag('onclick', job_url_elements)

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
            job_url = "https:" + job_url.replace("location.href=", "").replace("'", "")
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    carturesti = carturestiScraper()
    carturesti.get_response()
    carturesti.scrape_jobs()
    carturesti.sent_to_future()
    
    

