#
#
#
# ramadaiasi > http://www.ramadaiasi.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class ramadaiasiScraper(BS4Scraper):
    
    """
    A class for scraping job data from ramadaiasi website.
    """
    url = 'http://www.ramadaiasi.ro/cariere/'
    url_logo = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/ramadaiasi.png'
    company_name = 'ramadaiasi'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)
        
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
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")
            self.job_count += 1

if __name__ == "__main__":
    ramadaiasi = ramadaiasiScraper()
    ramadaiasi.get_response()
    ramadaiasi.scrape_jobs()
    ramadaiasi.sent_to_future()
    
    

