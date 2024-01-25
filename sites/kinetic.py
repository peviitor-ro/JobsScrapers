#
#
#
# kinetic > https://www.kinetic.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class kineticScraper(BS4Scraper):
    
    """
    A class for scraping job data from kinetic website.
    """
    url = 'https://www.kinetic.ro/cariere/'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/kinetic.PNG'
    company_name = 'kinetic'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from kinetic website.
        """

        job_elements = self.get_jobs_elements('css_', 'div:nth-child(2) > div > p > strong')
        
        self.job_titles = self.get_jobs_details_text(job_elements)

        self.format_data()
        # print(self.job_titles)
        
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
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", ["Iasi", "Bucuresti", "Cluj-Napoca"])
            self.job_count += 1

if __name__ == "__main__":
    kinetic = kineticScraper()
    kinetic.get_response()
    kinetic.scrape_jobs()
    kinetic.sent_to_future()
    
    

