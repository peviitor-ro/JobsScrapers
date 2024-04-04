#
#
#
# atpgroup > https://atp-group.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class atpgroupScraper(BS4Scraper):
    
    """
    A class for scraping job data from atpgroup website.
    """
    url = 'https://atp-group.ro/cariere/'
    url_logo = 'https://atp-group.ro/wp-content/uploads/2022/09/logo.svg'
    company_name = 'atpgroup'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from atpgroup website.
        """

        job_elements = self.get_jobs_elements('css_', "div.elementor-element.elementor-element-63afff4.elementor-widget.elementor-widget-theme-post-title.elementor-page-title.elementor-widget-heading > div > h3 > a")
        job_location_elements = self.get_jobs_elements('class_', 'elementor-icon-list-items elementor-post-info')
        
        self.job_cities = []
        
        for city in self.get_jobs_details_text(job_location_elements):
            if city.split("Companie:")[0].replace("Locație: ", "") == '':
                self.job_cities.append("Romania")
            else:
                self.job_cities.append(city.split("Companie:")[0].replace("Locație: ", ""))
        
        self.job_titles = self.get_jobs_details_text(job_elements)
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
        regiune_sud = ['Bucuresti', 'Ilfov', 'Călărași', 'Ialomița', 'Constanța']
        regiune_sud_vest = ['Dolj', 'Olt', 'Vâlcea', 'Mehedinți']
        regiune_vest = ['Hunedoara', 'Alba', 'Caraș-Severin', 'Arad', 'Timișoara']
        
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            if "Vest" in job_title:
                job_city = regiune_vest
            elif "Sud-Vest" in job_title:
                job_city = regiune_sud_vest
            elif "Sud" in job_title:
                job_city = regiune_sud
            else:
                job_city = job_city[:-1].replace("Cluj", "Cluj-Napoca")
                
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    atpgroup = atpgroupScraper()
    atpgroup.get_response()
    atpgroup.scrape_jobs()
    atpgroup.sent_to_future()
    
    

