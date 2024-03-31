#
#
#
# rombat > https://www.rombat.ro/ro/companie/careers/


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

    def scrape_jobs(self):
        """
        Scrape job data from rombat website.  Extrage datele locurilor de muncă de pe site-ul rombat.
        """

        job_title_elements = self.get_jobs_elements('css_', 'li.cms-singleline-control')

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
