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

        job_elements = self.get_jobs_elements('css_', 'div.cm-job')
        
        self.job_titles = []
        self.job_urls = []
        
        for job in job_elements:
            title_elem = job.find('b')
            if title_elem:
                self.job_titles.append(title_elem.text.strip())
            
            link_elem = job.find('a', class_='cm-btn')
            if link_elem and link_elem.get('href'):
                self.job_urls.append(link_elem.get('href'))
            else:
                self.job_urls.append('')

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
    
    

