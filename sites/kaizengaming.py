#
#
#
# KaizenGaming > https://kaizengaming.com/open-positions/


from sites.website_scraper_bs4 import BS4Scraper

class KaizenGamingScraper(BS4Scraper):
    
    """
    A class for scraping job data from KaizenGaming website.
    """
    url = 'https://kaizengaming.com/open-positions/'
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

        job_titles_elements = self.get_jobs_elements('class_', 'position')
        job_cities_elements = self.get_jobs_elements('class_', 'location')
        job_urls_elements = self.get_jobs_elements('css_', 'td.position > a')
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)
        self.job_countries = self.job_cities
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
        for job_title, job_url, job_country, job_city in zip(self.job_titles, self.job_urls, self.job_countries, self.job_cities):
            if job_country == 'Bucharest':
                job_country = "România"
            if job_url and job_country == 'România':
                self.create_jobs_dict(job_title, job_url, job_country, job_city)

if __name__ == "__main__":
    KaizenGaming = KaizenGamingScraper()
    KaizenGaming.get_response()
    KaizenGaming.scrape_jobs()
    KaizenGaming.sent_to_future()
    
    

