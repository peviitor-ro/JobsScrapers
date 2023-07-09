#
#
#
# InterbrandsOrbico > https://interbrandsorbico.recruitee.com/#section-72572


from sites.website_scraper_bs4 import BS4Scraper

class InterbrandsOrbicoScrapper(BS4Scraper):
    
    """
    A class for scraping job data from InterbrandsOrbico website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.website_url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.website_url)
    
    def scrape_jobs(self):
        """
        Scrape job data from InterbrandsOrbico website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "title")
        locations = self.get_jobs_elements('css_', "li[class='location']")
        job_urls = self.get_jobs_elements('class_', "col-md-6")
        
        job_cities = self.get_jobs_details_text(locations)
        job_countries = self.get_jobs_details_text(locations)
        
        self.job_cities = []
        self.job_countries = []
        
        for city, country in zip(job_cities, job_countries):
            self.job_countries.append(country.replace(",", "").split()[-1])
            self.job_cities.append(city.replace(",", "").replace(country.split()[-1], "")[:-1])
            
            
        self.job_titles = self.get_jobs_details_text(job_titles_elements)
        self.job_urls = self.get_jobs_details_href(job_urls)
        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city, job_country in zip(self.job_titles, self.job_urls, self.job_cities, self.job_countries):
            job_url = f"https://interbrandsorbico.recruitee.com{job_url}"
            self.create_jobs_dict(job_title, job_url, job_country, job_city)

if __name__ == "__main__":
    URL = 'https://interbrandsorbico.recruitee.com/#section-72572'
    URL_LOGO = 'https://d27i7n2isjbnbi.cloudfront.net/careers/photos/270715/thumb_photo_1658741832.png'
    company_name = 'InterbrandsOrbico'
    InterbrandsOrbico = InterbrandsOrbicoScrapper(company_name, URL, URL_LOGO)
    InterbrandsOrbico.get_response()
    InterbrandsOrbico.scrape_jobs()
    InterbrandsOrbico.sent_to_future()
    
    

