#
#
#
# ipso > https://www.ipso.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class ipsoScraper(BS4Scraper):
    
    """
    A class for scraping job data from ipso website.
    """
    url = 'https://www.ipso.ro/cariere/'
    url_logo = 'https://www.ipso.ro/wp-content/uploads/2020/09/logo-IPSO-Agricultura-bun.png'
    company_name = 'ipso'
    
    
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
        Scrape job data from ipso website.
        """

        job_elements = self.get_jobs_elements('css_', 'div:nth-child(1) > div > p:nth-child(1) > strong')
        job_cities_elements = self.get_jobs_elements('css_', 'div:nth-child(1) > div > p:nth-child(2) > strong')
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)

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
        for job_title, job_city in zip(self.job_titles, self.job_cities):
            if job_city == "Divizia Moldova":
                continue
            elif job_city.lower() == 'toate judetele tarii' or job_city == "TOATE JUDEȚELE ȚĂRII":
                job_city = "all"
            elif job_city == "Târgu Mureș":
                job_city = "Targu Mures"
            
            job_url = self.url + "#" + str(self.job_count)
            
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace("Târgu Mureș", "Targu Mures").replace("Piatra Neamț", "Piatra-Neamț").replace("Mihai Kogalniceanu", "Mihail Kogalniceanu").split(", "))
            self.job_count += 1

if __name__ == "__main__":
    ipso = ipsoScraper()
    ipso.get_response()
    ipso.scrape_jobs()
    ipso.sent_to_future()
    
    

