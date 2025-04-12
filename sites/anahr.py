#
#
#
# anahr > https://anahr.ro/domenii/joburi-pe-domenii/

from sites.website_scraper_bs4 import BS4Scraper

class anahrScraper(BS4Scraper):
    
    """
    A class for scraping job data from anahr website.
    """
    url = 'https://anahr.ro/domenii/joburi-pe-domenii/page/'
    url_logo = 'https://anahr.ro/wp-content/uploads/2023/01/logo-01.svg'
    company_name = 'anahr'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from anahr website.
        """
        error_text = []
        self.job_titles = []
        self.job_urls = []
        count_page = 1
        
        while error_text != ['Se pare că nu s-a găsit nimic în această locație. Poate încercați o căutare?']:
            self.get_content(f"https://anahr.ro/domenii/joburi-pe-domenii/page/{count_page}")
            job_titles_elements = self.get_jobs_elements('class_', 'uk-link-reset')
            job_urls_elements = self.get_jobs_elements('class_', "el-link uk-button uk-button-primary")
            
            self.job_titles.extend(self.get_jobs_details_text(job_titles_elements))
            self.job_urls.extend(self.get_jobs_details_href(job_urls_elements))
            
            error_text = self.get_jobs_details_text(self.get_jobs_elements('class_', 'uk-text-large uk-text-center uk-margin-large-bottom'))
            
            count_page += 1


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

#if __name__ == "__main__":
    #anahr = anahrScraper()
    #anahr.get_response()
    #anahr.scrape_jobs()
    #anahr.sent_to_future()
    
    

