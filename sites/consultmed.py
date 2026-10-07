#
#
#
# consultmed > https://consultmed.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class consultmedScraper(BS4Scraper):
    
    """
    A class for scraping job data from consultmed website.
    """
    url = 'https://consultmed.ro/cariere/'
    url_logo = 'https://new.consultmed.ro/wp-content/uploads/2025/11/logo7-215x88-1.png'
    company_name = 'consultmed'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from consultmed website.
        """

        self.job_titles = []
        self.job_urls = []

        heading = None
        for tag in self.soup.find_all(['h1', 'h2', 'h3', 'h4']):
            if 'Posturi deschise' in tag.get_text():
                heading = tag
                break

        container = heading.find_parent('div') if heading else None
        grid = container.find('div', style=lambda s: s and 'display:grid' in s) if container else None
        job_elements = grid.find_all('div', recursive=False) if grid else []

        for job in job_elements:
            title_elem = job.find('b')
            if not title_elem:
                for span in job.find_all('span'):
                    if span.find('svg') is None:
                        title_elem = span
                        break
            if not title_elem:
                continue

            title = title_elem.get_text(strip=True)
            if not title:
                continue

            self.job_titles.append(title)

            link_elem = job.find('a', href=True)
            if link_elem:
                self.job_urls.append(link_elem.get('href'))
            else:
                self.job_urls.append(self.url)

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
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")

if __name__ == "__main__":
    consultmed = consultmedScraper()
    consultmed.get_response()
    consultmed.scrape_jobs()
    consultmed.sent_to_future()
    
    

