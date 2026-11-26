#
#
#
# artvertising > https://www.artvertising.com.ro/cariere

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from sites.website_scraper_bs4 import BS4Scraper

class artvertisingScraper(BS4Scraper):
    
    """
    A class for scraping job data from artvertising website.
    """
    url = 'https://www.artvertising.com.ro/cariere'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/artvertising.PNG'
    company_name = 'artvertising'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
        options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        driver = webdriver.Chrome(options=options)
        try:
            driver.get(self.url)
            WebDriverWait(driver, 60).until(
                lambda browser: browser.title and 'One moment' not in browser.title
            )
            self.soup = BeautifulSoup(driver.page_source, 'lxml')
        finally:
            driver.quit()
    
    def scrape_jobs(self):
        """
        Scrape job data from artvertising website.
        """

        job_elements = self.get_jobs_elements(
            'css_', "body > div:nth-child(6) > div h4 a[href^='/cariere/']")
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)

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
            job_url = f"https://www.artvertising.com.ro{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    artvertising = artvertisingScraper()
    artvertising.get_response()
    artvertising.scrape_jobs()
    artvertising.sent_to_future()
    
    

