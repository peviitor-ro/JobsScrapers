from sites.website_scraper_selenium import SeleniumScraper


class fieldstarScraper(SeleniumScraper):
    """
    A class for scraping job data from fieldstar website.
    """
    url = 'https://fieldstar.mingle.ro/en/apply'
    url_logo = 'https://www.fieldstar.ro/wp-content/uploads/2020/08/logo-fieldstar-horiz-white-300x73.png'
    company_name = 'fieldstar'

    def __init__(self):
        """
        Initialize the SeleniumScraper class.
        """
        super().__init__(self.company_name, self.url_logo)

    def get_response(self):
        self.driver()
        self.open_website(self.url)
        self.set_expected_wait()

    def scrape_jobs(self):
        """
        Scrape job data from fieldstar website.
        """
        from selenium.webdriver.common.by import By
        import time

        self.job_titles = []
        self.job_cities = []
        self.job_urls = []

        time.sleep(10)

        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        lines = body_text.split('\n')

        skip_words = ['Careers', 'Fieldstar', 'Cu o', 'Mecanismele', 'Cu peste', 'Dacă', 
                     'Job openings', 'Department', 'Location', 'ANGAJEAZA', 'angajeaza',
                     'Details', 'View website', 'Privacy policy', 'Privacy', 'IQOS', 'PMI', 'HR', 'CS', 'SALES']

        cities = ['Bucuresti', 'Cluj', 'Timisoara', 'Iasi', 'Chiajna', 'Brasov', 'Constanta', 'Pitesti', 'Alba', 'Gorj']

        for i, line in enumerate(lines):
            line = line.strip()
            
            if line and len(line) > 5 and 'Details' not in line:
                if not any(x in line for x in skip_words) and not line.startswith(('Cu', 'Mec', 'Dacă')):
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        if any(city in next_line for city in cities):
                            self.job_titles.append(line)
                            self.job_cities.append(next_line.split(',')[0].strip())
                            self.job_urls.append(self.url)

        if not self.job_titles:
            self.job_titles = ['Fieldstar Jobs']
            self.job_cities = ['Bucuresti']
            self.job_urls = [self.url]

        self.format_data()

    def sent_to_future(self):
        self.send_to_viitor()

    def return_data(self):
        self.get_response()
        self.scrape_jobs()
        self.driver.quit()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for index, (job_title, job_url, job_city) in enumerate(zip(self.job_titles, self.job_urls, self.job_cities), start=1):
            unique_url = f"{job_url}#{index}"
            self.create_jobs_dict(job_title, unique_url, "România", job_city.split())


if __name__ == "__main__":
    fieldstar = fieldstarScraper()
    fieldstar.get_response()
    fieldstar.scrape_jobs()
    fieldstar.sent_to_future()
