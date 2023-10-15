#
#
#
# sonrisatechnologies > https://www.careers.sonrisa.hu/#jobs

from sites.website_scraper_bs4 import BS4Scraper

class sonrisatechnologiesScraper(BS4Scraper):
    
    """
    A class for scraping job data from sonrisatechnologies website.
    """
    url = 'https://www.careers.sonrisa.hu/#jobs'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/sonrisa.PNG'
    company_name = 'sonrisatechnologies'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from sonrisatechnologies website.
        """

        job_titles_elements = self.get_jobs_elements('class_', 'text-block-base-link sm:min-w-[25%] sm:truncate company-link-style')
        job_urls_elements = self.get_jobs_elements('class_', "hover:bg-block-base-text hover:bg-opacity-3 flex flex-col sm:flex-row justify-between items-center py-4 px-6")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
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
            self.create_jobs_dict(job_title, job_url, "România", "Oradea")

if __name__ == "__main__":
    sonrisatechnologies = sonrisatechnologiesScraper()
    sonrisatechnologies.get_response()
    sonrisatechnologies.scrape_jobs()
    sonrisatechnologies.sent_to_future()
    
    

