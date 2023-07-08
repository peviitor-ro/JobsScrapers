#
#
#
# cargotrack > https://cargotrack.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class cargotrackScrapper(BS4Scraper):
    
    """
    A class for scraping job data from cargotrack website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.website_url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.website_url)
    
    def scrape_jobs(self):
        """
        Scrape job data from cargotrack website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "div > div.awsm-list-left-col > h2 > a")[1:]
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_titles_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Oradea")

if __name__ == "__main__":
    URL = 'https://cargotrack.ro/cariere/'
    URL_LOGO = 'https://i0.wp.com/cargotrack.ro/wp-content/uploads/2022/03/logo.jpg?fit=1449%2C406&ssl=1'
    company_name = 'cargotrack'
    cargotrack = cargotrackScrapper(company_name, URL, URL_LOGO)
    cargotrack.get_response()
    cargotrack.scrape_jobs()
    cargotrack.sent_to_future()
    
    

