#
#
#
# expomedics > https://www.expomedics.com/jobs?country=romania

from sites.website_scraper_bs4 import BS4Scraper

class expomedicsScrapper(BS4Scraper):
    
    """
    A class for scraping job data from expomedics website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from expomedics website.
        """
        
        self.job_titles = []
        self.job_urls = []
        
            
        page_count = self.get_jobs_details_text(self.get_jobs_elements('css_', "div.col-12.col-lg-3.d-none.d-lg-inline > div > p"))[0].split()[-1]
        for page in range(1, int(page_count)+2):
            job_elements = self.get_jobs_elements('class_', "job-link")
            self.job_titles.extend(self.get_jobs_details_text(job_elements))
            self.job_urls.extend(self.get_jobs_details_href(job_elements))
            self.get_content(self.url + f"&page={page}")


        

        self.format_data()
        # print(self.job_titles, len(self.job_titles))
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "România")

if __name__ == "__main__":
    URL = 'https://www.expomedics.com/jobs?country=romania'
    URL_LOGO = 'https://www.expomedics.com/img/logo.png'
    company_name = 'expomedics'
    expomedics = expomedicsScrapper(company_name, URL, URL_LOGO)
    expomedics.get_response()
    expomedics.scrape_jobs()
    expomedics.sent_to_future()
    
    

