#
#
#
# trencadis > https://trencadis.ro/cariere.html

from sites.website_scraper_bs4 import BS4Scraper

class trencadisScrapper(BS4Scraper):
    
    """
    A class for scraping job data from trencadis website.
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
        Scrape job data from trencadis website.
        """

        job_elements = self.get_jobs_elements('class_', 'pdfLink')
        
        self.job_titles = self.get_jobs_details_text(job_elements)
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
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "Romania", "Bucuresti")

if __name__ == "__main__":
    URL = 'https://trencadis.ro/cariere.html'
    URL_LOGO = 'https://i0.1616.ro/media/2/2621/33206/21112260/2/trencadis.jpg?width=514'
    company_name = 'trencadis'
    trencadis = trencadisScrapper(company_name, URL, URL_LOGO)
    trencadis.get_response()
    trencadis.scrape_jobs()
    trencadis.sent_to_future()
    
    

