#
#
#
# InterbrandsOrbico > https://interbrandsorbico.recruitee.com/#section-72572


from sites.website_scraper_bs4 import BS4Scraper

class InterbrandsOrbicoScraper(BS4Scraper):
    
    """
    A class for scraping job data from InterbrandsOrbico website.
    """
    url = 'https://interbrandsorbico.recruitee.com/#section-72572'
    url_logo = 'https://d27i7n2isjbnbi.cloudfront.net/careers/photos/270715/thumb_photo_1658741832.png'
    company_name = 'InterbrandsOrbico'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from InterbrandsOrbico website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "sc-6exb5d-1 jnZALp")
        locations = self.get_jobs_elements('class_', "custom-css-style-job-location")
        job_urls = self.get_jobs_elements('class_', "sc-s03za1-0 iCILJS")
        
        job_cities = self.get_jobs_details_text(locations)
        job_countries = self.get_jobs_details_text(locations)
        
        self.job_cities = []
        self.job_countries = []
        
        for city, country in zip(job_cities, job_countries):
            self.job_countries.append(country.replace(",", "").split()[-1])
            self.job_cities.append(city.replace(",", "").replace("•", "").replace("Bitrita", "Bistrita").replace(country.split()[-1], "")[:-1])
            
            
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls)
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
        for job_title, job_url, job_city, job_country in zip(self.job_titles, self.job_urls, self.job_cities, self.job_countries):
            job_url = f"https://interbrandsorbico.recruitee.com{job_url}"
            if job_country == "Romania":
                job_country = "România"
            if job_city == "Targu Mures":
                job_city = "Targu-Mures"
            self.create_jobs_dict(job_title, job_url, job_country, job_city)

if __name__ == "__main__":
    InterbrandsOrbico = InterbrandsOrbicoScraper()
    InterbrandsOrbico.get_response()
    InterbrandsOrbico.scrape_jobs()
    InterbrandsOrbico.sent_to_future()
    
    

