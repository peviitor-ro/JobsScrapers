#
#
#
# conlan > https://conlangrup.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper


class conlanScraper(BS4Scraper):
    """
    A class for scraping job data from conlan website.
    """
    url = 'https://conlangrup.ro/cariere/'
    url_logo = 'https://conlangrup.ro/wp-content/uploads/2018/09/logo.png'
    company_name = 'conlan'

    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        self.job_urls = []
        super().__init__(self.company_name, self.url_logo)

    def get_response(self):
        self.get_content(self.url)

    def scrape_jobs(self):
        """
        Scrape job data from conlan website.  Extrage datele locurilor de muncă de pe site-ul conlan.
        """

        job_title_elements =  self.get_jobs_elements('css_',
                                                  'a[href="https://conlangrup.ro/job/project-manager/"]')

        self.job_url_elements = self.get_jobs_elements('css_',
                                                  'a[href="https://conlangrup.ro/job/project-manager/"], a[href="https://conlangrup.ro/job/inginer-constructii/"]')

        self.job_titles = self.get_jobs_details_text(job_title_elements)

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
        for job_element in self.job_url_elements:
            job_title = job_element.text.strip()
            job_url = job_element.get('href').strip()

            if job_title and job_url and not job_title.startswith('+ detalii'):
                job_url = f"https://conlangrup.ro/cariere/{job_url}"
                self.create_jobs_dict(job_title, job_url, "România", "Sibiu")


if __name__ == "__main__":
    conlan = conlanScraper()
    conlan.get_response()
    conlan.scrape_jobs()
    conlan.sent_to_future()