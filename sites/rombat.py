#
#
#
# rombat > https://www.rombat.ro/cariere


import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from sites.website_scraper_bs4 import BS4Scraper


class rombatScraper(BS4Scraper):
    """
    A class for scraping job data from rombat website.
    """
    url = 'https://www.rombat.ro/cariere'
    url_en = 'https://www.rombat.ro/en/careers/'
    url_logo = 'https://www.rombat.ro/Uploads/Images/Banner-Website.jpg'
    company_name = 'rombat'

    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)

    def get_content_with_retry(self, url, max_retries=5):
        self._set_headers()
        session = requests.Session()
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,
            status_forcelist=[104, 429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        response = session.get(url, headers=self.DEFAULT_HEADERS, verify=False, timeout=60)
        self.soup = BeautifulSoup(response.content, 'lxml')

    def get_response(self):
        self.get_content_with_retry(self.url)
        # Pagina românească de cariere poate fi goală după migrarea site-ului,
        # însă joburile sunt publicate și pe pagina engleză de cariere.
        if not self.soup.select('.jobs__list .job'):
            self.get_content_with_retry(self.url_en)

    def scrape_jobs(self):
        """
        Scrape job data from rombat website.  Extrage datele locurilor de muncă de pe site-ul rombat.
        """

        self.job_titles = []
        self.job_urls = []
        self.job_cities = []

        for job in self.soup.select('.jobs__list .job'):
            title_element = job.find('h3')
            title = title_element.get_text(strip=True) if title_element else ''
            if not title:
                continue

            city = 'Bistrita'
            details = job.select('dt')
            values = job.select('dd')
            for detail, value in zip(details, values):
                if 'Loca' in detail.get_text(strip=True):
                    city = value.get_text(strip=True).title() or city
                    break

            job_url = ''
            for link in job.select('a.button'):
                href = (link.get('href') or '').strip()
                if href.startswith('http'):
                    job_url = href
                    break
            if not job_url:
                job_url = self.url + "#" + str(self.job_count)

            self.job_titles.append(title)
            self.job_urls.append(job_url)
            self.job_cities.append(city)

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
        Iterează peste toate detaliile locurilor de muncă și le trimite la dicționarul de locuri de muncă.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)
            self.job_count += 1


if __name__ == "__main__":
    rombat = rombatScraper()
    rombat.get_response()
    rombat.scrape_jobs()
    rombat.sent_to_future()
