#
#
#
#
# Qubiz > https://qubiz.com/careers


from sites.website_scraper_selenium import SeleniumScraper
from selenium.webdriver.common.by import By
import time


class QubizScraper(SeleniumScraper):
    
    """
    A class for scraping job data from Qubiz website.
    """
    url = 'https://qubiz.com/careers'
    url_logo = 'https://assets-global.website-files.com/603e16fd5761f8f7787bf39a/64491d149607dd73d0e80235_LogoWebsiteAnniversary.svg'
    company_name = 'Qubiz'
    
    def __init__(self):
        """
        Initialize the SeleniumScraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.driver()
        self.open_website(self.url)
        self.set_expected_wait()
        time.sleep(10)
        
    def scrape_jobs(self):
        """
        Scrape job data from Qubiz website.
        """
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        self.job_remotes = []
        
        # Get the page source and parse with BeautifulSoup
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        
        # Job cards are server rendered <li class="cr-card"> entries
        for card in soup.select('li.cr-card'):
            title_element = card.select_one('h3.cr-card-title')
            link_element = card.select_one('a[href*="/careers/"]')
            meta_element = card.select_one('p.cr-card-meta')
            
            if not title_element or not link_element:
                continue
            
            title = title_element.get_text(strip=True)
            href = link_element.get('href', '').strip()
            meta = meta_element.get_text(' ', strip=True) if meta_element else ''
            
            if not title or not href:
                continue
            
            # meta format: "Cluj-Napoca, Oradea, Hybrid | Senior"
            location = meta.split('|')[0]
            cities = []
            remote = 'on-site'
            
            for place in (part.strip() for part in location.split(',')):
                if not place:
                    continue
                lowered = place.lower()
                if lowered == 'remote':
                    remote = 'remote'
                elif lowered == 'hybrid':
                    remote = 'hybrid'
                else:
                    cities.append(place)
            
            if not cities:
                cities = ['Oradea']
            
            full_url = href if href.startswith('http') else f"https://qubiz.com{href}"
            self.job_titles.append(title)
            self.job_cities.append(cities)
            self.job_urls.append(full_url)
            self.job_remotes.append(remote)
        
        self.format_data()
        
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
        for job_title, job_url, job_city, job_remote in zip(
            self.job_titles, self.job_urls, self.job_cities, self.job_remotes
        ):
            self.create_jobs_dict(job_title, job_url, "România", job_city, job_remote)

if __name__ == "__main__":
    Qubiz = QubizScraper()
    Qubiz.get_response()
    Qubiz.scrape_jobs()
    Qubiz.sent_to_future()
