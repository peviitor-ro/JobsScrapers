#
#
#
# deltatelgroup > https://deltatelgroup.com/ro/cariere


from sites.website_scraper_bs4 import BS4Scraper

class deltatelgroupScraper(BS4Scraper):
    
    """
    A class for scraping job data from deltatelgroup website.
    """
    url = 'https://deltatelgroup.com/ro/cariere'
    url_logo = 'https://deltatelgroup.com/templates/deltatel/images/deltatel.png'
    company_name = 'deltatelgroup'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        self.soup = None
        
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
            self._set_headers()
            response = session.get(self.url, headers=self.DEFAULT_HEADERS, verify=False, timeout=(5, 30))
            self.soup = self.parse_content(response.content)
        except requests.exceptions.RequestException:
            self.soup = None
    
    def parse_content(self, content):
        from bs4 import BeautifulSoup
        return BeautifulSoup(content, 'lxml')
    
    def scrape_jobs(self):
        """
        Scrape job data from deltatelgroup website.
        """
        if self.soup is None:
            return

        job_titles_elements = self.soup.select("h2 > a")
        self.job_titles = [' '.join(el.text.split()) for el in job_titles_elements]
        self.job_links = [' '.join(el.get('href').split()) for el in job_titles_elements]

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
        for job_title, job_url in zip(self.job_titles, self.job_links):
            job_url = f"https://deltatelgroup.com/{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", ['Cluj-Napoca', 'Bucuresti'])

if __name__ == "__main__":
    deltatelgroup = deltatelgroupScraper()
    deltatelgroup.get_response()
    deltatelgroup.scrape_jobs()
    deltatelgroup.sent_to_future()
