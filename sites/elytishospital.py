#
#
#
# elytishospital > https://elytis-hospital.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class elytishospitalScraper(BS4Scraper):
    
    """
    A class for scraping job data from elytishospital website.
    """
    url = 'https://elytis-hospital.ro/cariere/'
    url_logo = 'https://elytis-hospital.ro/wp-content/uploads/2023/08/logo-1-scaled-2.png'
    company_name = 'elytishospital'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from elytishospital website.
        """

        job_elements = self.get_jobs_elements('css_', "h3.job-title > a")
        
        self.job_titles = []
        self.job_urls = []
        
        for elem in job_elements:
            self.job_titles.append(elem.text.strip())
            self.job_urls.append(elem.get('href'))

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
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    elytishospital = elytishospitalScraper()
    elytishospital.get_response()
    elytishospital.scrape_jobs()
    elytishospital.sent_to_future()
    
    

