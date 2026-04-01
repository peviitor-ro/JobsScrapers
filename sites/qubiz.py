#
#
#
#
# Qubiz > https://qubiz.com/jobs


from sites.website_scraper_selenium import SeleniumScraper
from selenium.webdriver.common.by import By
import time


class QubizScraper(SeleniumScraper):
    
    """
    A class for scraping job data from Qubiz website.
    """
    url = 'https://qubiz.com/jobs?page=1'
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
        
        # Get the page source and parse with BeautifulSoup
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        
        # Find job links
        job_links = soup.find_all('a', href=lambda h: h and '/jobs/' in h and h != 'https://qubiz.com/jobs')
        
        for link in job_links:
            href = link.get('href', '')
            
            # Get title from h4 or h6
            h4 = link.find('h4')
            h6 = link.find('h6')
            title = h4.text.strip() if h4 else (h6.text.strip() if h6 else '')
            
            if not title:
                # Try getting from parent
                title = link.text.strip()
            
            if title and href:
                full_url = f"https://qubiz.com{href}"
                self.job_titles.append(title)
                self.job_cities.append('Oradea')  # Qubiz is based in Oradea, Romania
                self.job_urls.append(full_url)
        
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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    Qubiz = QubizScraper()
    Qubiz.get_response()
    Qubiz.scrape_jobs()
    Qubiz.sent_to_future()
