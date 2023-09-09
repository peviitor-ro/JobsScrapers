#
#
#
# ramadaiasi > http://www.ramadaiasi.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class ramadaiasiScrapper(BS4Scraper):
    
    """
    A class for scraping job data from ramadaiasi website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        self.job_count = 1
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from ramadaiasi website.
        """

        job_elements = self.get_jobs_elements('css_', '#content-section-1 > div > div:nth-child(1) > p')
        
        self.job_titles = self.get_jobs_details_text(job_elements)[0].replace("Alatura-te acum echipei noastre aplicand pentru unul din posturile vacante: ", "").replace(". Trimite-ne datele tale – nume, prenume, adresa, telefon, e-mail, CV-ul, o fotografie recenta – mentioneaza jobul dorit si te vom contacta.", "").split(", ")

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")
            self.job_count += 1

if __name__ == "__main__":
    URL = 'http://www.ramadaiasi.ro/cariere/'
    URL_LOGO = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/ramadaiasi.png'
    company_name = 'ramadaiasi'
    ramadaiasi = ramadaiasiScrapper(company_name, URL, URL_LOGO)
    ramadaiasi.get_response()
    ramadaiasi.scrape_jobs()
    ramadaiasi.sent_to_future()
    
    

