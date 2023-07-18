#
#
#
# titanmachinery > https://www.titanmachinery.ro/en/pag/careers?page=

from sites.website_scraper_bs4 import BS4Scraper

class titanmachineryScrapper(BS4Scraper):
    
    """
    A class for scraping job data from titanmachinery website.
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
        Scrape job data from titanmachinery website.
        """
        
        job_elements = self.get_jobs_elements('css_', "div > div.news-info-list > div.news-title-list > a")
        self.job_titles = []
        self.job_urls = []
        self.job_cities = []
        page_counter = 2

        # Itterate over pages and get the title, city url append them to list afterwards
        while job_elements:
            job_elements = self.get_jobs_elements('css_', "div > div.news-info-list > div.news-title-list > a")
            if len(job_elements) >= 1:
                # Titles
                self.job_titles.extend(self.get_jobs_details_text(job_elements))
                
                # Cities
                # self.job_city.extend(self.get_jobs_details_text(job_elements).replace("[perioadă determinată]", "").split()[-1])
                for job_city in self.get_jobs_details_text(job_elements):
                    self.job_cities.append(job_city.replace("[perioadă determinată]", "").split()[-1])
                    
                # URLS
                self.job_urls.extend(self.get_jobs_details_href(job_elements))
                
                # Next Page content
                self.get_content(f"{self.url}{page_counter}")
            page_counter += 1

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://www.titanmachinery.ro/en/pag/careers?page='
    URL_LOGO = 'https://www.titanmachinery.ro/images/default_image_categories.png'
    company_name = 'titanmachinery'
    titanmachinery = titanmachineryScrapper(company_name, URL, URL_LOGO)
    titanmachinery.get_response()
    titanmachinery.scrape_jobs()
    titanmachinery.sent_to_future()
