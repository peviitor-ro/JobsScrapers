#
#
#
# ensemblesoftware > https://www.ensemblesoftware.ro/careers/


from sites.website_scraper_bs4 import BS4Scraper

class ensemblesoftwareScrapper(BS4Scraper):
    
    """
    A class for scraping job data from ensemblesoftware website.
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
        Scrape job data from ensemblesoftware website.
        """

        job_elements = self.get_jobs_elements('class_', 'opportunities__link')
        
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
            job_url = f"https://www.ensemblesoftware.ro/{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", ['Baia Mare', 'Brasov', 'Cluj'])

if __name__ == "__main__":
    URL = 'https://www.ensemblesoftware.ro/careers/'
    URL_LOGO = 'https://www.directmm.ro/wp-content/uploads/2021/08/ensembleLogo-blue-large.png'
    company_name = 'ensemblesoftware'
    ensemblesoftware = ensemblesoftwareScrapper(company_name, URL, URL_LOGO)
    ensemblesoftware.get_response()
    ensemblesoftware.scrape_jobs()
    ensemblesoftware.sent_to_future()
    
    

