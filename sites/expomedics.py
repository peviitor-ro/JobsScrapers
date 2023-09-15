#
#
#
# expomedics > https://www.expomedics.com/jobs?country=romania

from sites.website_scraper_bs4 import BS4Scraper

class expomedicsScraper(BS4Scraper):
    
    """
    A class for scraping job data from expomedics website.
    """
    url = 'https://www.expomedics.com/jobs?country=romania'
    url_logo = 'https://www.expomedics.com/img/logo.png'
    company_name = 'expomedics'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)
        
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
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "România")
            self.job_count += 1

if __name__ == "__main__":
    expomedics = expomedicsScraper()
    expomedics.get_response()
    expomedics.scrape_jobs()
    expomedics.sent_to_future()
    
    

