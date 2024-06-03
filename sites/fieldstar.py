from sites.website_scraper_bs4 import BS4Scraper


class fieldstarScraper(BS4Scraper):
    """
    A class for scraping job data from fieldstar website.
    """
    url = 'https://www.fieldstar.ro/j/'  # URL-ul paginii de cariere
    url_logo = 'https://www.fieldstar.ro/wp-content/uploads/2020/08/logo-fieldstar-horiz-white-300x73.png'
    company_name = 'fieldstar'

    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)

    def get_response(self):
        self.get_content(self.url)

    def scrape_jobs(self):
        """
        Scrape job data from fieldstar website.
        """
        job_title_elements = self.get_jobs_elements('class_', "awsm-job-post-title")
        job_link_elements = self.get_jobs_elements('class_', "awsm-job-item")

        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_links = self.get_jobs_details_href(job_link_elements)

        # Extragem și orașele
        city_elements = self.get_jobs_elements('class_', "awsm-job-specification-locatie")
        self.job_cities = self.get_jobs_details_text(city_elements)

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
        for job_title, job_link, job_city in zip(self.job_titles, self.job_links, self.job_cities):
            if job_city.lower() == 'remote':
                job_city = 'all'
            self.create_jobs_dict(job_title, job_link, "România", job_city.split())


if __name__ == "__main__":
    fieldstar = fieldstarScraper()
    fieldstar.get_response()
    fieldstar.scrape_jobs()
    fieldstar.sent_to_future()
