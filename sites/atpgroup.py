#
#
#
# atpgroup > https://atp-group.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class atpgroupScraper(BS4Scraper):
    
    """
    A class for scraping job data from atpgroup website.
    """
    url = 'https://atp-group.ro/cariere/cauta'
    url_logo = 'https://atp-group.ro/wp-content/uploads/2022/09/logo.svg'
    company_name = 'atpgroup'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from atpgroup website.
        """

        job_elements = self.get_jobs_elements('css_', "#jobs .accordion-item")
        
        self.job_titles = []
        self.job_urls = []
        self.job_cities = []
        
        for job in job_elements:
            headers = job.select('.job-header')
            if len(headers) >= 3:
                title = headers[0].get_text(strip=True)
                company = headers[1].get_text(strip=True)
                city = headers[2].get_text(strip=True)
                
                job_link = job.select_one('a.btn-secondary')
                job_url = job_link.get('href') if job_link else ''
                
                self.job_titles.append(title)
                self.job_cities.append(city)
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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_city = job_city.replace("Cluj", "Cluj-Napoca") if job_city else "România"
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    atpgroup = atpgroupScraper()
    atpgroup.get_response()
    atpgroup.scrape_jobs()
    atpgroup.sent_to_future()
