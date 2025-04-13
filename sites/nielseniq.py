#
# 
#
# nielseniq > https://nielseniq.com/?s=&market=global&language=en&orderby=&order=&post_type=career_job&job_locations=romania&job_teams=&job_types=


from sites.website_scraper_bs4 import BS4Scraper

class nielseniqScraper(BS4Scraper):
    
    """
    A class for scraping job data from nielseniq website.
    """
    url = 'https://nielseniq.com/?s=&market=global&language=en&orderby=&order=&post_type=career_job&job_locations=romania&job_teams=&job_types='
    url_logo = 'https://c.smartrecruiters.com/sr-company-images-prod-aws-dc5/5f20077aa2b8ac7a5a26cb93/c83a18a7-1926-4be1-9572-10cc0fbdc9b3/huge?r=s3-eu-central-1&_1677595339802'
    company_name = 'nielseniq'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from nielseniq website.
        """
        
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        
        job_counter_element = self.get_jobs_elements('css_', "a[href^='https://nielseniq.com/page/']")
        job_counter = self.get_jobs_details_href(job_counter_element)
        
        while job_counter:

            job_title_elements = self.get_jobs_elements('class_', 'entry-title')
            job_city_elements = self.get_jobs_elements('css_', 'header > div:nth-child(2) > span:nth-child(1)')
            job_url_elements = self.get_jobs_elements('class_', 'card-cover-link')

            self.job_titles.extend(self.get_jobs_details_text(job_title_elements))
            self.job_cities.extend(self.get_jobs_details_text(job_city_elements))
            self.job_urls.extend(self.get_jobs_details_href(job_url_elements))

            job_counter_element = self.get_jobs_elements('css_', "a[href^='https://nielseniq.com/page/']")
            job_counter = self.get_jobs_details_href(job_counter_element)
            if job_counter:
                self.get_content(job_counter[0])
        
        # If the initial loop didn't get triggered due to missing next page element
        if not job_counter:
            job_title_elements = self.get_jobs_elements('class_', 'entry-title')
            job_city_elements = self.get_jobs_elements('css_', 'header > div:nth-child(2) > span:nth-child(1)')
            job_url_elements = self.get_jobs_elements('class_', 'card-cover-link')

            self.job_titles.extend(self.get_jobs_details_text(job_title_elements))
            self.job_cities.extend(self.get_jobs_details_text(job_city_elements))
            self.job_urls.extend(self.get_jobs_details_href(job_url_elements))

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
        # This jobs are hybrid model which are hard coded due to the unstructured page
        exception_jobs = ['Research Consultant']
        
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            if job_title in exception_jobs:
                remote = 'hybrid'
            else:
                remote = 'on-site'
                
            if job_city == "Bucharest":
                job_city = "București"
            self.create_jobs_dict(job_title, job_url, "România", job_city, remote)

#if __name__ == "__main__":
    #nielseniq = nielseniqScraper()
    #nielseniq.get_response()
    #nielseniq.scrape_jobs()
    #nielseniq.sent_to_future()
    
    

