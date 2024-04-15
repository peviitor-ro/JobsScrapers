#
#
#
# berg > https://www.berg-software.com/en/join-us/


from sites.website_scraper_bs4 import BS4Scraper


class bergScraper(BS4Scraper):
    """
    A class for scraping job data from aeroportoradea website.
    """
    url = 'https://www.berg-software.com/en/join-us/'
    url_logo = 'https://berg-software.com/wp-content/uploads/berg-software-logo-116x60px-optimised.png'
    company_name = 'berg'

    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)

    def get_response(self):
        self.get_content(self.url)

    def scrape_jobs(self):
        """
        Scrape job data from berg-software website.
        """
        job_title_elements = self.get_jobs_elements('css_', '.awsm-job-post-title')
        job_url_elements = self.get_jobs_elements('class_', 'awsm-job-item')

        self.job_titles = self.get_jobs_details_text(job_title_elements)
        self.job_urls = self.get_jobs_details_href(job_url_elements)

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
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "Romania", "Timisoara", "remote")


if __name__ == "__main__":
    berg = bergScraper()
    berg.get_response()
    berg.scrape_jobs()
    berg.sent_to_future()
