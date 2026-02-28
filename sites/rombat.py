#
#
#
# rombat > https://www.rombat.ro/cariere


from sites.website_scraper_bs4 import BS4Scraper


class rombatScraper(BS4Scraper):
    """
    A class for scraping job data from rombat website.
    """
    url = 'https://www.rombat.ro/ro/companie/careers/'
    url_logo = 'https://www.rombat.ro/Uploads/Images/Banner-Website.jpg'
    company_name = 'rombat'

    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)

    def get_response(self):
        self.get_content(self.url)

    url = 'https://www.rombat.ro/cariere'
    
    def scrape_jobs(self):
        """
        Scrape job data from rombat website.  Extrage datele locurilor de muncă de pe site-ul rombat.
        """

        self.job_titles = []
        
        # Find h2 with 'Joburi ROMBAT' and get job titles from following elements
        h2 = self.soup.find('h2', string=lambda x: x and 'Joburi ROMBAT' in x)
        if h2:
            # Find all h3 elements with job titles
            for h3 in h2.find_all_next('h3'):
                text = h3.get_text(strip=True)
                if text and len(text) > 5:
                    self.job_titles.append(text)

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
        Iterează peste toate detaliile locurilor de muncă și le trimite la dicționarul de locuri de muncă.
        """
        for job_title in self.job_titles:
            if 'APLICA AICI' in job_title:
                job_url = job_title.split('APLICA AICI')[-1][1:].replace("www.", "https://")
                job_title = job_title.split('APLICA AICI')[0].split("\u2013")[0]
            else:
                job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Bistrita")
            self.job_count += 1



if __name__ == "__main__":
    rombat = rombatScraper()
    rombat.get_response()
    rombat.scrape_jobs()
    rombat.sent_to_future()
