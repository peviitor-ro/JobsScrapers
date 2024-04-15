#
#
#
# titanmachinery > https://www.titanmachinery.ro/en/pag/careers?page=

from sites.website_scraper_bs4 import BS4Scraper

class titanmachineryScraper(BS4Scraper):
    
    """
    A class for scraping job data from titanmachinery website.
    """
    url = 'https://www.titanmachinery.ro/en/pag/careers?page='
    url_logo = 'https://www.titanmachinery.ro/images/default_image_categories.png'
    company_name = 'titanmachinery'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from titanmachinery website.
        """
        
        job_elements = self.get_jobs_elements('css_', "div > div.news-info-list > div.news-title-list > a")
        self.job_titles, self.job_urls, self.job_cities = [], [], []
        
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

        # Get cities from right side of screen
        city_pages_elements = self.get_jobs_elements('css_', "div.left-menu > ul > li > a")
        city_pages_links = self.get_jobs_details_href(city_pages_elements)
        
        
        # Itterate over pages and get the title, city url append them to list afterwards
        for city_link in city_pages_links:
            self.get_content(city_link)
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
                # self.get_content(f"{self.url}{page_counter}")
                # self.get_content(f"{self.url}{page_counter}")
            # page_counter += 1


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
        exception_jobs = {
            "Ilfov":["Voluntari","Buftea","Pantelimon","Popesti Leordeni","Jilava","Chitila","Otopeni","Bragadiru","Branesti","Afumati","Peris","Balotesti","Domnesti","Magurele","1 Decembrie","Mogosoaia","Cornetu","Berceni","Moara Vlasiei","Chiajna","Glina","Clinceni","Vidra","Dobroesti","Tunari","Darasti-Ilfov","Copaceni","Ciorogarla","Ciolpani","Rosu","Cretesti","Fundeni","Tanganu","Catelu","Silistea Snagovului","Cernica","Lipia","Dragomiresti-Deal","Sintesti","Buciumeni","Balaceanca","Stefanestii de Jos","Gruiu","Gradistea","Varteju","Ghermanesti","Dascalu","Darvari","Caciulati","Burias","Stefanestii de Sus","Snagov","Tancabesti","Tamasi","Piteasca","Petrachioaia","Islaz","Alunisu","Rudeni","Corbeanca","Merii Petchii","Caldararu","Olteni","Dragomiresti-Vale","Saftica","Zurbaua","Sitaru","Ciofliceni","Sindrilita","Piscu","Pasarea","Micsunestii Mari","Dudu","Nuci","Cozieni","Dumitrana","Ganeasa","Izvorani","Posta","Moara Domneasca","Santu Floresti","Teghes","Micsunestii-Moara","Gagu","Maineasca","Vanatori","Balteni","Petresti","Surlari","Ostratu","Dumbraveni","Luparia","Manolache","Balta Neagra","Pruni","Cretuleasca","Vladiceasca","Creata","Runcu","Vadu Anei","Buda","Dimieni","Odaile","Ordoreanu"]
            }
        
        passed_titles = []
        passed_urls = []
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            if "-" not in job_city:
                job_city = job_title.split()[-1]
            elif "Ilfov" in job_city:
                job_city = exception_jobs['Ilfov']
            if job_title not in passed_titles and job_url not in passed_urls:
                self.create_jobs_dict(job_title, job_url, "România", job_city.replace("Cluj", "Cluj-Napoca").replace("CLUJ", "Cluj-Napoca").replace("(", "").replace(")", ""))
            passed_titles.append(job_title)
            passed_urls.append(job_url)

if __name__ == "__main__":
    titanmachinery = titanmachineryScraper()
    titanmachinery.get_response()
    titanmachinery.scrape_jobs()
    # titanmachinery.sent_to_future()
