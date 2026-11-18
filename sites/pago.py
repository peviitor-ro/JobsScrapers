#
#
#
# Pago > https://pago.ro/en/jobs


from urllib.parse import urljoin

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from sites.website_scraper_bs4 import BS4Scraper


class PagoScraper(BS4Scraper):

    url = 'https://pago.ro/en/jobs'
    url_logo = 'https://besticon-demo.herokuapp.com/lettericons/P-120-6a4397.png'
    company_name = 'Pago'

    def __init__(self):
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
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': """
                    Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                    Object.defineProperty(navigator, 'appVersion', {get: () => '5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'});
                    Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
                    Object.defineProperty(navigator, 'plugins', {get: () => {
                        let plugins = Object.create(PluginArray.prototype);
                        Object.defineProperty(plugins, 'length', {value: 1});
                        plugins[0] = Object.create(Plugin.prototype);
                        return plugins;
                    }});
                    Object.defineProperty(navigator, 'mimeTypes', {get: () => {
                        let mimeTypes = Object.create(MimeTypeArray.prototype);
                        Object.defineProperty(mimeTypes, 'length', {value: 1});
                        mimeTypes[0] = Object.create(MimeType.prototype);
                        return mimeTypes;
                    }});
                """
            })
            driver.get(self.url)
            WebDriverWait(driver, 30).until(
                lambda browser: browser.find_elements(By.CSS_SELECTOR, 'a.btn-secondary-outline')
            )
            self.soup = BeautifulSoup(driver.page_source, 'lxml')
        finally:
            driver.quit()

    def scrape_jobs(self):
        self.job_titles = []
        self.job_urls = []

        for a_tag in self.soup.find_all('a', class_='btn-secondary-outline'):
            href = a_tag.get('href', '')
            if href == 'https://revolutpeople.com/pago/public/careers':
                continue

            job_card = a_tag.find_parent('div')
            title_span = job_card.find('span', style=lambda v: 'font-weight: 700' in (v or ''))
            if title_span:
                self.job_titles.append(title_span.get_text(strip=True))
                self.job_urls.append(urljoin('https://pago.ro', href))

        self.format_data()

    def sent_to_future(self):
        self.send_to_viitor()

    def return_data(self):
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Bucuresti", "remote")


if __name__ == "__main__":
    Pago = PagoScraper()
    Pago.get_response()
    Pago.scrape_jobs()
    Pago.sent_to_future()
    
    

