#
# 
#
# softing > https://career.softing.com/open-positions/job-opportunities/softing-romania.html


from sites.website_scraper_bs4 import BS4Scraper

class softingScrapper(BS4Scraper):
    
    """
    A class for scraping job data from softing website.
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
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            job_url = f"https://career.softing.com{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://career.softing.com/open-positions/job-opportunities/softing-romania.html'
    URL_LOGO = 'https://career.softing.com/typo3conf/ext/softingtheme/Resources/Public/Images/logo.png'
    company_name = 'softing'
    softing = softingScrapper(company_name, URL, URL_LOGO)
    softing.get_response()
    softing.scrape_jobs()
    softing.sent_to_future()
    
    

