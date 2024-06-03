from sites.website_scraper_bs4 import BS4Scraper


class alumilScraper(BS4Scraper):
    """
    A class for scraping job data from alumil website.
    """
    url = 'https://www.alumil.com/romania/corporate/careers/job-openings'  # URL-ul paginii de cariere
    url_logo = 'https://www.alumil.com/ResourcePackages/Alumil/assets/dist/images/logo.svg'
    company_name = 'alumil'

    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)

    def get_response(self):
        self.get_content(self.url)

    def scrape_jobs(self):
        """
        Scrape job data from alumil website.
        """
        job_title_elements = self.get_jobs_elements('class_', "article-title")
        job_link_elements = self.get_jobs_elements('css_', "div.col-xs-1.article-arrow > a")

        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_links = self.get_jobs_details_href(job_link_elements)

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
        for job_title, job_link in zip(self.job_titles, self.job_links):
            job_city = "București"  # Hardcodăm orașul companiei -> București
            self.create_jobs_dict(job_title, job_link, "România", [job_city])


if __name__ == "__main__":
    alumil = alumilScraper()
    alumil.get_response()
    alumil.scrape_jobs()
    alumil.sent_to_future()
