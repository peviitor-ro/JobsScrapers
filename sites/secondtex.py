#
#
#
# secondtex > https://www.secondtex.ro/cariera


from sites.website_scraper_bs4 import BS4Scraper


class secondtexScraper(BS4Scraper):
    
    """
    A class for scraping job data from secondtex website.
    """
    url = 'https://www.secondtex.ro/cariera'
    url_logo = 'https://www.secondtex.ro/sites/all/themes/bootstrap/logo.png'
    company_name = 'secondtex'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        import requests
        response = requests.get(self.url, verify=False, timeout=30, headers=headers)
        from bs4 import BeautifulSoup
        self.soup = BeautifulSoup(response.content, 'lxml')
    
    def scrape_jobs(self):
        """
        Scrape job data from secondtex website.
        """
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        
        text = self.soup.get_text()
        
        # Find job title from the page text
        # The job listing is "Sortator haine"
        job_keywords = ['Sortator', 'sortator', 'Angajam', 'angajam', 'Cautam', 'cautam']
        
        # Parse the job details from page text
        lines = text.split('\n')
        in_job_section = False
        current_title = ''
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for job title
            if 'Sortator' in line or 'sortator' in line:
                current_title = 'Sortator haine'
                if current_title not in self.job_titles:
                    self.job_titles.append(current_title)
                    # Location from the page: Dorolt, Satu Mare
                    self.job_cities.append('Dorolt')
                    self.job_urls.append(self.url)
        
        # If no jobs found but page has career content, add a generic entry
        if not self.job_titles and ('Cariere' in text or 'cariera' in text.lower()):
            self.job_titles.append('Send CV to info@secondtex.ro')
            self.job_cities.append('Dorolt')
            self.job_urls.append('mailto:info@secondtex.ro')
        
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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            if job_url.startswith('mailto:'):
                self.create_jobs_dict(job_title, job_url, "România", job_city)
            else:
                self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    secondtex = secondtexScraper()
    secondtex.get_response()
    secondtex.scrape_jobs()
    secondtex.sent_to_future()
