#
#
#
# softexco > https://softexco.ro/p/cariere#aplica

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from sites.website_scraper_bs4 import BS4Scraper

class softexcoScraper(BS4Scraper):
    
    """
    A class for scraping job data from softexco website.
    """
    url = 'https://softexco.ro/p/cariere'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/softexco.PNG'
    company_name = 'softexco'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--window-size=1400,900')
        options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

        driver = webdriver.Chrome(options=options)
        try:
            driver.get(self.url)
            WebDriverWait(driver, 30).until(
                lambda browser: browser.find_elements(By.CSS_SELECTOR, 'p.position')
            )
            self.soup = BeautifulSoup(driver.page_source, 'lxml')
        finally:
            driver.quit()
    
    def scrape_jobs(self):
        """
        Scrape job data from softexco website.
        """

        # Get the jobs
        job_titles_elements = self.get_jobs_elements('class_', "position")
        job_link_elements = self.get_jobs_elements('class_', "careers-button")
        
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_link_elements)

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
            job_url = f"{self.url}{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", "Cluj-Napoca")

if __name__ == "__main__":
    softexco = softexcoScraper()
    softexco.get_response()
    softexco.scrape_jobs()
    softexco.sent_to_future()
    
    

