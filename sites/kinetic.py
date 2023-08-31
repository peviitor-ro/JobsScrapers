#
#
#
# kinetic > https://www.kinetic.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class kineticScrapper(BS4Scraper):
    
    """
    A class for scraping job data from kinetic website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        self.job_count = 1
        super().__init__(company_name, company_logo_url)
        
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
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", ["Iasi", "Bucuresti", "Cluj"])
            self.job_count += 1

if __name__ == "__main__":
    URL = 'https://www.kinetic.ro/cariere/'
    URL_LOGO = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/kinetic.PNG'
    company_name = 'kinetic'
    kinetic = kineticScrapper(company_name, URL, URL_LOGO)
    kinetic.get_response()
    kinetic.scrape_jobs()
    kinetic.sent_to_future()
    
    

