#
#
#
# carturesti > https://carturesti.ro/info/joburi

from sites.website_scraper_bs4 import BS4Scraper

class carturestiScrapper(BS4Scraper):
    
    """
    A class for scraping job data from carturesti website.
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
        Scrape job data from carturesti website.
        """

        job_title_elements = self.get_jobs_elements('css_', 'div:nth-child(7) > div > h2')
        job_location_elements = self.get_jobs_elements('css_', 'tr:nth-child(2) > td:nth-child(2)')
        job_url_elements = self.get_jobs_elements('class_', 'job-button')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)[:-1]
        self.job_cities = self.get_jobs_details_text(job_location_elements)
        self.job_urls = self.get_jobs_details_tag('onclick', job_url_elements)[:-1]

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
            job_url = "https:" + job_url.replace("location.href=", "").replace("'", "")
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://carturesti.ro/info/joburi'
    URL_LOGO = 'https://shopniac.ro/wp-content/uploads/2016/06/logo-libraria-carturesti.jpg'
    company_name = 'carturesti'
    carturesti = carturestiScrapper(company_name, URL, URL_LOGO)
    carturesti.get_response()
    carturesti.scrape_jobs()
    carturesti.sent_to_future()
    
    

