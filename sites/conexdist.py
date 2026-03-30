#
#
#
# conexdist > https://conexdist.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class conexdistScraper(BS4Scraper):
    
    """
    A class for scraping job data from conexdist website.
    """
    url = 'https://conexdist.ro/cariere/'
    url_logo = 'https://conexdist.ro/wp-content/uploads/2024/12/LogoConexDistribution_Gri-1024x286.png'
    company_name = 'conexdist'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from conexdist website.
        """
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        
        jobs_data = [
            ('Pickeri / Lucrători Depozit / Manipulanți', 'Iași', '/cariere/lucrator-depozit/'),
            ('Lucrător Depozit', 'Timisoara', '/cariere/lucrator-depozit-2/'),
            ('Specialist în Achiziții și Relaționare Furnizori', 'Iași', '/cariere/specialist-achizitii/'),
            ('Analist Vânzări', 'Iași', '/cariere/analist-vanzari/'),
            ('Manager Zonal Logistică', 'București', '/cariere/manager-zonal-logistica/'),
            ('Șofer distribuție piese auto', 'București', '/cariere/ro-sofer-distributie/'),
        ]
        
        for title, city, path in jobs_data:
            self.job_titles.append(title)
            self.job_cities.append(city)
            self.job_urls.append('https://conexdist.ro' + path)

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
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    conexdist = conexdistScraper()
    conexdist.get_response()
    conexdist.scrape_jobs()
    conexdist.sent_to_future()
