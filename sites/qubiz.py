#
#
#
#
## Qubiz > https://www.qubiz.com/jobs

from sites.website_scraper_bs4 import BS4Scraper
import time

class QubizScraper(BS4Scraper):
    
    """
    A class for scraping job data from Qubiz website.
    """
    url = 'https://qubiz.com/jobs?page=1'
    url_logo = 'https://assets-global.website-files.com/603e16fd5761f8f7787bf39a/64491d149607dd73d0e80235_LogoWebsiteAnniversary.svg'
    company_name = 'Qubiz'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Qubiz website.
        """

        page = 1
        job_titles_elements = []
        job_urls_elements = []
        job_cities_elements = []

        while True:
            titles = self.get_jobs_elements('css_', 'a > h4')
            urls = self.get_jobs_elements('css_', 'div.flex.flex-col > div > a')
            cities = self.get_jobs_elements('css_', 'a > h6')

            if not titles:
                break  # Exit loop if no job elements found

            job_titles_elements.extend(titles)
            job_urls_elements.extend(urls)
            job_cities_elements.extend(cities)

            page += 1
            self.url = f"https://qubiz.com/jobs?page={page}"
            self.get_response()
            time.sleep(30)
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)
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
        job_country = "Romania"
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_city = job_city.split(" | ")[0].split(", ")
            if "Remote" in job_city:
                remote = 'remote'
                job_city.remove("Remote")
            elif "Hybrid" in job_city:
                remote = 'hybrid'
                job_city.remove("Hybrid")
            else:
                remote = 'on-site'
            job_url = f"https://qubiz.com{job_url}"
            self.create_jobs_dict(job_title, job_url, job_country, job_city, remote=remote, county=None)

if __name__ == "__main__":
    Qubiz = QubizScraper()
    Qubiz.get_response()
    Qubiz.scrape_jobs()
    Qubiz.sent_to_future()
    
    

