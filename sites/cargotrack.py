#
#
#
# cargotrack > https://cargotrack.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class cargotrackScraper(BS4Scraper):
    
    """
    A class for scraping job data from cargotrack website.
    """
    url = 'https://cargotrack.ro/cariere/'
    url_logo = 'https://i0.wp.com/cargotrack.ro/wp-content/uploads/2022/03/logo.jpg?fit=1449%2C406&ssl=1'
    company_name = 'cargotrack'
    
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
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        try:
            response = session.get(self.url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
            }, verify=False, timeout=(5, 30))
            from bs4 import BeautifulSoup
            self.soup = BeautifulSoup(response.content, 'lxml')
        except requests.exceptions.RequestException:
            self.soup = None
    
    def scrape_jobs(self):
        """
        Scrape job data from cargotrack website.
        """
        if self.soup is None:
            return

        job_cards = self.get_jobs_elements('css_', ".card")
        
        self.job_titles = []
        self.job_urls = []
        
        for card in job_cards:
            card_text = card.get_text(separator=' | ', strip=True)
            parts = card_text.split(' | ')
            
            if len(parts) >= 2:
                title = parts[1].strip()
                
                links = card.select('a')
                job_url = ''
                for link in links:
                    href = link.get('href', '')
                    if href and href not in ['/vreau-sa-lucrez-la-cargotrack/', '/angajam-contabil-economist/']:
                        if href.startswith('http'):
                            job_url = href
                        elif href.startswith('/'):
                            job_url = 'https://cargotrack.ro' + href
                        break
                
                if title and title != 'Vreau să lucrez la CargoTrack':
                    self.job_titles.append(title)
                    self.job_urls.append(job_url)

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
            self.create_jobs_dict(job_title, job_url, "România", "Oradea")

if __name__ == "__main__":
    cargotrack = cargotrackScraper()
    cargotrack.get_response()
    cargotrack.scrape_jobs()
    cargotrack.sent_to_future()
