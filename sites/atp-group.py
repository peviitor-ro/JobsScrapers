#
#
#
# atpgroup > https://www.distributie-energie.ro/despre-noi/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class atpgroupScrapper(BS4Scraper):
    
    """
    A class for scraping job data from atpgroup website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.website_url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.website_url)
    
    def scrape_jobs(self):
        """
        Scrape job data from atpgroup website.
        """

        job_elements = self.get_jobs_elements('css_', "div.elementor-element.elementor-element-63afff4.elementor-widget.elementor-widget-theme-post-title.elementor-page-title.elementor-widget-heading > div > h3 > a")
        job_location_elements = self.get_jobs_elements('class_', 'elementor-post-info__terms-list-item')
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_cities = self.get_jobs_details_text(job_location_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)

        self.format_data()
        print(self.job_cities)
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://atp-group.ro/cariere/'
    URL_LOGO = 'https://atp-group.ro/wp-content/uploads/2022/09/logo.svg'
    company_name = 'atpgroup'
    atpgroup = atpgroupScrapper(company_name, URL, URL_LOGO)
    atpgroup.get_response()
    atpgroup.scrape_jobs()
    atpgroup.sent_to_future()
    
    

