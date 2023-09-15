#
#
#
# secondtex > https://www.secondtex.ro/ro/loc-de-munca

from sites.website_scraper_bs4 import BS4Scraper

class secondtexScraper(BS4Scraper):
    
    """
    A class for scraping job data from secondtex website.
    """
    url = 'https://www.secondtex.ro/ro/loc-de-munca'
    url_logo = 'https://www.secondtex.ro/sites/all/themes/bootstrap/logo.png'
    company_name = 'secondtex'
    
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
        Scrape job data from secondtex website.
        """

        # Get the jobs
        job_titles_elements = self.get_jobs_elements('class_', "el-head animated bounceIn go")
        self.job_titles = self.get_jobs_details_text(job_titles_elements)

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
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title.replace("Secondtex angajeaza: ", ""), job_url, "România", "Dorolt")
            self.job_count += 1

if __name__ == "__main__":
    secondtex = secondtexScraper()
    secondtex.get_response()
    secondtex.scrape_jobs()
    secondtex.sent_to_future()
    
    

