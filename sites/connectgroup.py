#
#
#
# connectgroup > https://www.connectgroup.com/en/vacancies/roemeni%C3%AB

from sites.website_scraper_bs4 import BS4Scraper

class connectgroupScraper(BS4Scraper):
    
    """
    A class for scraping job data from connectgroup website.
    """
    url = 'https://www.connectgroup.com/en/vacancies/roemeni%C3%AB'
    url_logo = 'https://www.connectgroup.com/images/logo-connectgroup.svg'
    company_name = 'connectgroup'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from connectgroup website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'job__text__title')
        job_countries_elements = self.get_jobs_elements('class_', 'job__text__country')
        job_urls_elements = self.get_jobs_elements('class_', "job")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)[:-1]
        self.job_countries = self.get_jobs_details_text(job_countries_elements)[:-1]
        self.job_urls = [job_url.replace("ë", "%C3%AB") for job_url in self.get_jobs_details_href(job_urls_elements)[:-1]]

        self.format_data()
        print(self.job_urls, len(self.job_urls))
        
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
        for job_title, job_country, job_url in zip(self.job_titles, self.job_countries, self.job_urls):
            self.create_jobs_dict(job_title, job_url, job_country.replace("Romania", "România"), "Oradea")

if __name__ == "__main__":
    connectgroup = connectgroupScraper()
    connectgroup.get_response()
    connectgroup.scrape_jobs()
    connectgroup.sent_to_future()
    
    

