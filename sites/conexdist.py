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

        job_row_elements = self.get_jobs_elements('css_', 'div.row[id^="row-1094412602"] > div')
        
        self.job_titles = []
        self.job_urls = []
        self.job_cities = []
        
        for row in job_row_elements:
            title_elem = row.find('h3')
            if title_elem:
                text = title_elem.get_text(separator=' ', strip=True)
                if text and "Nu ai găsit" not in text:
                    self.job_titles.append(text)
                    self.job_urls.append(self.url)
                    
                    city_elem = row.find('p')
                    if city_elem:
                        city_text = city_elem.get_text(separator=' ', strip=True).replace('Sediul Central', '').replace('&#8211;', '').strip()
                        cities = [c.strip() for c in city_text.split(',')]
                        city = cities[0] if cities else ""
                        self.job_cities.append(city)
                    else:
                        self.job_cities.append("")

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
    
    

