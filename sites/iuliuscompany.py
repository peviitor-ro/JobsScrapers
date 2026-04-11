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

        job_cards = self.soup.select("div.box-oferta")
        
        for card in job_cards:
            title_elem = card.select_one("h2")
            city_elem = card.select_one("div.locatie")
            link_elem = card.select_one("a")
            
            if title_elem and city_elem and link_elem:
                job_title = ' '.join(title_elem.text.split())
                job_city = ' '.join(city_elem.text.split()).replace("LOCAȚIE: ", "").replace("Cluj", "Cluj-Napoca")
                job_url = self.url + link_elem.get('href', '')
                
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
    
    

