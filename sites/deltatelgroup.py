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
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from deltatelgroup website.
        """

        job_titles_elements = self.get_jobs_elements('css_', "h2 > a")

        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_links = self.get_jobs_details_href(job_titles_elements)

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
    
    

