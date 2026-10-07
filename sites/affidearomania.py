#
# 
#
# affidearomania > https://affidearomania.recruitee.com/


from sites.website_scraper_bs4 import BS4Scraper

class affidearomaniaScraper(BS4Scraper):
    
    """
    A class for scraping job data from affidearomania website.
    """
    url = 'https://affidearomania.recruitee.com'
    url_logo = 'https://jurmed.ro/medici/wp-content/uploads/sites/2/2023/02/1.-Affidea.png'
    company_name = 'affidearomania'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from affidearomania website.
        """

        location_pairs = [
            (
                job_city.find_previous(
                    'a', href=lambda href: href and href.startswith('/o/')
                ),
                job_city,
            )
            for job_city in self.get_jobs_elements(
                'class_', 'custom-css-style-job-location-city'
            )
        ]
        location_pairs = [
            (job_element, job_city)
            for job_element, job_city in location_pairs
            if job_element is not None
        ]

        job_elements = [job_element for job_element, _ in location_pairs]
        job_cities_elements = [job_city for _, job_city in location_pairs]

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
        seen_job_urls = set()
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            job_url = self.url + job_url
            if job_url in seen_job_urls:
                continue
            seen_job_urls.add(job_url)
            if "Complex Cosmopolis" in job_city:
                job_city = "Bucuresti"
            self.create_jobs_dict(job_title, job_url, "România", job_city.replace(", Romania", "").replace("PIATRA NEAMT", "Piatra-Neamt").split(", "))

if __name__ == "__main__":
    affidearomania = affidearomaniaScraper()
    affidearomania.get_response()
    affidearomania.scrape_jobs()
    affidearomania.sent_to_future()
    
    

