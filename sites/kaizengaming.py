#
#
#
# KaizenGaming > https://kaizengaming.com/open-positions/


from sites.website_scraper_bs4 import BS4Scraper

class KaizenGamingScraper(BS4Scraper):
    
    """
    A class for scraping job data from KaizenGaming website.
    """
    url = 'https://boards.greenhouse.io/embed/job_board?for=kaizengaming'
    url_logo = 'https://kaizengaming.com/wp-content/uploads/2022/11/Logo_KaizenGaming_Colour.svg'
    company_name = 'KaizenGaming'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from KaizenGaming website.
        """

        job_elements = self.get_jobs_elements('css_', "a[href^='https://careers.kaizengaming.com/job-details/']")
        job_cities_elements = self.get_jobs_elements('class_', 'location')
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)
        
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
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            if 'Romania' in job_city:
                job_city = job_city.split(", ")[0].replace("Bucharest", "Bucuresti")
            else:
                continue
            
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    KaizenGaming = KaizenGamingScraper()
    KaizenGaming.get_response()
    KaizenGaming.scrape_jobs()
    KaizenGaming.sent_to_future()
    
    

