#
#
#
# ipso > https://monnoyeur.wd103.myworkdayjobs.com/ro-RO/Monnoyeur


from sites.website_scraper_selenium import SeleniumScraper
from selenium.webdriver.common.by import By
import time


class ipsoScraper(SeleniumScraper):
    
    """
    A class for scraping job data from ipso website.
    """
    url = 'https://monnoyeur.wd103.myworkdayjobs.com/ro-RO/Monnoyeur?hiringCompany=e9240506062810102069e15158e50000'
    url_logo = 'https://www.ipso.ro/wp-content/uploads/2020/09/logo-IPSO-Agricultura-bun.png'
    company_name = 'ipso'
    
    def __init__(self):
        """
        Initialize the SeleniumScraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.driver()
        self.open_website(self.url)
        self.set_expected_wait()
        time.sleep(15)
        
    def scrape_jobs(self):
        """
        Scrape job data from ipso website.
        """
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        
        for link in links:
            href = link.get_attribute('href') or ''
            text = link.text.strip()
            
            if '/job/' in href and href.startswith('https://monnoyeur.wd103.myworkdayjobs.com/ro-RO/Monnoyeur/job/'):
                if text and text not in self.job_titles:
                    city = href.split('/job/')[1].split('/')[0].replace('-', ' ')
                    city = self._normalize_city(city)
                    
                    self.job_titles.append(text)
                    self.job_cities.append(city)
                    self.job_urls.append(href)
        
        self.format_data()
        
    def _normalize_city(self, city):
        city_mapping = {
            'CHITILA': 'Chitila',
            'ORADEA IPS': 'Oradea',
            'CRAIOVA IPS': 'Craiova',
            'ALBA IULIA': 'Alba Iulia',
            'MOGOSOAIA IPS': 'Mogosoaia',
            'TARGU MURES IPS': 'Targu-Mures',
            'LUMINA': 'Lumina',
            'ALEXANDRIA': 'Alexandria',
            'FETESTI': 'Fetesti',
            'CALARASI': 'Calarasi',
            'BRAILA IPS': 'Braila',
            'TIMISOARA IPS': 'Timisoara',
        }
        for key, value in city_mapping.items():
            if key in city.upper():
                return value
        return city
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.get_response()
        self.scrape_jobs()
        self.driver.quit()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)


if __name__ == "__main__":
    ipso = ipsoScraper()
    ipso.get_response()
    ipso.scrape_jobs()
    ipso.sent_to_future()
