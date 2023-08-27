#
#
#
# iasidelivery > https://iasi.delivery/cariere-horeca/


from sites.website_scraper_bs4 import BS4Scraper

class iasideliveryScrapper(BS4Scraper):
    
    """
    A class for scraping job data from iasidelivery website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        self.job_count = 1
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from iasidelivery website.
        """

        title_count = 2
        job_titles_elements = self.get_jobs_elements('id_', "Project_Enum2172_2953")
        self.job_titles = []
        
        # Itterate over a drop down and get all the titles until no more title elements exists
        while job_titles_elements:
            job_titles_elements = self.get_jobs_elements('css_', f"#Project_Enum2172_2953 > option:nth-child({title_count})")
            
            # If the list is not empty meaning jobs are available in the current targeted element append them to main list 
            if self.get_jobs_details_text(job_titles_elements) != []:
                self.job_titles.append(self.get_jobs_details_text(job_titles_elements)[0])
                
            title_count += 1
            

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")
            self.job_count += 1

if __name__ == "__main__":
    URL = 'https://iasi.delivery/cariere-horeca/'
    URL_LOGO = 'https://iasi.delivery/wp-content/uploads/2023/04/IasiDelivery_LOGO_HPositive-1.png'
    company_name = 'iasidelivery'
    iasidelivery = iasideliveryScrapper(company_name, URL, URL_LOGO)
    iasidelivery.get_response()
    iasidelivery.scrape_jobs()
    iasidelivery.sent_to_future()
    
    

