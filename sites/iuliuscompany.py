#
#
#
# iuliuscompany > https://cariere.iuliuscompany.ro/

from sites.website_scraper_bs4 import BS4Scraper

class iuliuscompanyScraper(BS4Scraper):
    
    """
    A class for scraping job data from iuliuscompany website.
    """
    url = 'https://cariere.iuliuscompany.ro'
    url_logo = 'https://ami.cname.ro/_/company/iulius-group/mediaPool/uK2z1mO.jpg'
    company_name = 'iuliuscompany'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        import requests
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        
        session = requests.Session()
        retry = Retry(total=1, connect=1, backoff_factor=0.3)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        try:
            self._set_headers()
            response = session.get(self.url, headers=self.DEFAULT_HEADERS, verify=False, timeout=3)
            from bs4 import BeautifulSoup
            self.soup = BeautifulSoup(response.content, 'lxml')
        except Exception as e:
            print(f"Error fetching content: {e}")
            self.soup = None
    
    def scrape_jobs(self):
        if self.soup is None:
            return

        job_cards = self.soup.select("div.border-eveniment")
        if not job_cards:
            job_cards = self.soup.select("div.box-oferta")

        for card in job_cards:
            link_elem = card.select_one("a[href*='oferta-job']")
            if not link_elem:
                link_elem = card.select_one("a")

            title_elem = card.select_one(".keywords-oferta a")
            if not title_elem:
                title_elem = card.select_one("h2")

            city_elem = card.select_one("div.locatie")
            if not city_elem:
                # sometimes location might be in a different element
                city_elem = card.select_one(".locatie-oferta") or card.select_one("span.locatie")

            if link_elem:
                href = link_elem.get('href', '')
                if href.startswith('http'):
                    job_url = href
                else:
                    job_url = self.url + href
            else:
                job_url = None

            if title_elem:
                job_title = ' '.join(title_elem.text.split())
            else:
                job_title = ' '.join(card.get_text(separator=' ', strip=True).split())[:100]

            if city_elem:
                job_city = ' '.join(city_elem.text.split()).replace("LOCAȚIE: ", "").replace("Locatie: ", "").replace("Cluj", "Cluj-Napoca")
            else:
                job_city = "România"

            if job_url and job_title:
                self.create_jobs_dict(job_title, job_url, "România", job_city)

        self.format_data()

    def format_data(self):
        pass
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

if __name__ == "__main__":
    iuliuscompany = iuliuscompanyScraper()
    iuliuscompany.get_response()
    iuliuscompany.scrape_jobs()
    iuliuscompany.sent_to_future()
    
    

