#
#
#
# aeroportoradea > https://www.aeroportoradea.ro/ro/locuri-de-munca-vacante.html


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from sites.website_scraper_bs4 import BS4Scraper

class aeroportoradeaScraper(BS4Scraper):
    
    """
    A class for scraping job data from aeroportoradea website.
    """
    url = 'https://www.aeroportoradea.ro/ro/locuri-de-munca-vacante.html'
    url_logo = 'https://www.aeroportoradea.ro/images/misc/logo-2021-01.svg'
    company_name = 'aeroportoradea'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(options=options)
        try:
            driver.get(self.url)
            try:
                WebDriverWait(driver, 30).until(
                    lambda d: "moment" not in d.title.lower()
                    and "please" not in d.title.lower()
                    and "vă rog" not in d.title.lower()
                )
            except Exception:
                pass
            self.soup = BeautifulSoup(driver.page_source, "lxml")
        finally:
            driver.quit()
    
    def scrape_jobs(self):
        """
        Scrape job data from aeroportoradea website.
        """

        article_elements = self.get_jobs_elements('css_', "article")
        
        self.job_titles = []
        self.job_urls = []
        for article in article_elements:
            title_element = article.select_one("h2")
            url_element = article.select_one("a[href*='docs/']")
            if title_element and url_element:
                self.job_titles.append(' '.join(title_element.text.split()))
                self.job_urls.append(' '.join(url_element.get('href').split()))

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
            if not job_url.startswith('http'):
                job_url = "https://www.aeroportoradea.ro/" + job_url.replace(" ", "%20")
            job_url = job_url + "#" + str(self.job_count)
            title = job_title.split("–")[0].split("-")[0].strip()
            self.create_jobs_dict(title, job_url, "România", "Oradea")
            self.job_count += 1

if __name__ == "__main__":
    aeroportoradea = aeroportoradeaScraper()
    aeroportoradea.get_response()
    aeroportoradea.scrape_jobs()
    aeroportoradea.sent_to_future()
    
    

