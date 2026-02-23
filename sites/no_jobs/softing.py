#
# 
#
# softing > https://career.softing.com/open-positions/job-opportunities/softing-romania.html


from sites.website_scraper_bs4 import BS4Scraper

class softingScraper(BS4Scraper):
    
    """
    A class for scraping job data from softing website.
    """
    url = 'https://career.softing.com/open-positions/job-opportunities/softing-romania.html'
    url_logo = 'https://career.softing.com/typo3conf/ext/softingtheme/Resources/Public/Images/logo.png'
    company_name = 'softing'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from softing website.
        """

        job_elements = self.get_jobs_elements('css_', 'tbody > tr > td > a')
        job_city_elements = self.get_jobs_elements('css_', '#c29496 >table > tbody > tr > td:nth-child(3)')
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_cities = self.get_jobs_details_text(job_city_elements)[1:]
        self.job_urls = self.get_jobs_details_href(job_elements)
        
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
            job_url = f"https://career.softing.com{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    softing = softingScraper()
    softing.get_response()
    softing.scrape_jobs()
    softing.sent_to_future()
    
    

