#
# 
#
# sinaps > https://www.sinaps.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class sinapsScraper(BS4Scraper):
    
    """
    A class for scraping job data from sinaps website.
    """
    url = 'https://www.sinaps.ro/cariere/'
    url_logo = 'https://www.sinaps.ro/wp-content/uploads/2018/05/rebrandingsinaps.jpg'
    company_name = 'sinaps'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from sinaps website.
        """

        job_title_elements = self.get_jobs_elements('css_', 'div.wpb_wrapper > h5')
        job_urls_elements = self.get_jobs_elements('css_', 'div.vc_general.vc_btn3')
        
        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_urls = self.get_jobs_details_href(job_urls_elements)
        
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
            self.create_jobs_dict(job_title.replace("Wanted: ", ""), job_url, "România", "Iasi")

if __name__ == "__main__":
    sinaps = sinapsScraper()
    sinaps.get_response()
    sinaps.scrape_jobs()
    sinaps.sent_to_future()
    
    

