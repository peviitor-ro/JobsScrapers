#
#
#
# panifcom > https://panifcom.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class panifcomScrapper(BS4Scraper):
    
    """
    A class for scraping job data from panifcom website.
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
        Scrape job data from panifcom website.
        """

        job_elements = self.get_jobs_elements('class_', 'd2edcug0')
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_cities = self.get_jobs_details_text(job_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_city in zip(self.job_titles, self.job_cities):
            job_city = job_city.split()[-1].replace("!", "")
            
            # This needs to be modified in the future
            job_title = job_title.replace("Căutăm ", "").replace("pentru ", "").replace("din ", "").replace("din ", "").replace("magazinele ", "").replace("noastre ", "").replace("personal", "").replace("postul", "").replace("de ", "").replace(",", "").replace(job_city, "").replace("  ", "")
            
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title[:-1], job_url, "România", job_city)
            self.job_count += 1

if __name__ == "__main__":
    URL = 'https://panifcom.ro/cariere/'
    URL_LOGO = 'https://panifcom.ro/wp-content/uploads/2020/01/panifcom-logo-sticky.png'
    company_name = 'panifcom'
    panifcom = panifcomScrapper(company_name, URL, URL_LOGO)
    panifcom.get_response()
    panifcom.scrape_jobs()
    panifcom.sent_to_future()
    
    

