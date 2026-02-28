#
#
#
# Pago > https://pago.ro/en/jobs


from sites.website_scraper_bs4 import BS4Scraper

class PagoScraper(BS4Scraper):
    
    """
    A class for scraping job data from Pago website.
    """
    url = 'https://pago.ro/en/jobs'
    url_logo = 'https://besticon-demo.herokuapp.com/lettericons/P-120-6a4397.png'
    company_name = 'Pago'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from Pago website.
        """

        section = self.soup.find('section', class_='hai-in-echipa')
        if section:
            text = section.get_text(separator='\n', strip=True)
            lines = text.split('\n')
            self.job_titles = []
            self.job_urls = []
            
            for line in lines:
                line = line.strip()
                if ' - ' in line and ('mid' in line.lower() or 'senior' in line.lower() or 'junior' in line.lower() or 'lead' in line.lower()):
                    job_title = line.split(' - ')[0].strip()
                    if job_title and len(job_title) > 3:
                        self.job_titles.append(job_title)
            
            for a in section.find_all('a', href=True):
                href = a.get('href', '')
                if 'bamboohr.com/careers/' in href:
                    self.job_urls.append(href)
        
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
            self.create_jobs_dict(job_title, job_url, "România", "Romania", "remote")

if __name__ == "__main__":
    Pago = PagoScraper()
    Pago.get_response()
    Pago.scrape_jobs()
    Pago.sent_to_future()
    
    

