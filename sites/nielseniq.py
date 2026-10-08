#
# 
#
# nielseniq > https://nielseniq.com/?s=&market=global&language=en&orderby=&order=&post_type=career_job&job_locations=&job_teams=&job_types=


from sites.website_scraper_bs4 import BS4Scraper

class nielseniqScraper(BS4Scraper):
    
    """
    A class for scraping job data from nielseniq website.
    """
    url = 'https://nielseniq.com/?s=&market=global&language=en&orderby=&order=&post_type=career_job&job_locations=&job_teams=&job_types='
    url_logo = 'https://c.smartrecruiters.com/sr-company-images-prod-aws-dc5/5f20077aa2b8ac7a5a26cb93/c83a18a7-1926-4be1-9572-10cc0fbdc9b3/huge?r=s3-eu-central-1&_1677595339802'
    company_name = 'nielseniq'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from nielseniq website.
        """
        
        self.job_titles = []
        self.job_cities = []
        self.job_countries = []
        self.job_urls = []
        
        while True:

            for job_element in self.get_jobs_elements('css_', 'article'):
                job_title_element = job_element.select_one('.entry-title')
                job_url_element = job_element.select_one('.card-cover-link')
                job_location_element = job_element.select_one('header > div:nth-child(2)')

                if not job_title_element or not job_url_element or not job_location_element:
                    continue

                location_terms = job_location_element.find_all('span', recursive=False)

                self.job_titles.append(' '.join(job_title_element.text.split()))
                self.job_urls.append(' '.join(job_url_element.get('href').split()))
                self.job_cities.append(' '.join(location_terms[0].text.split()) if location_terms else '')
                self.job_countries.append(' '.join(location_terms[1].text.split()) if len(location_terms) > 1 else '')

            next_page_elements = self.get_jobs_elements('css_', 'nav.number-pagination a.next.page-numbers')
            if not next_page_elements:
                break
            self.get_content(next_page_elements[0].get('href'))
        
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
        # This jobs are hybrid model which are hard coded due to the unstructured page
        exception_jobs = ['Research Consultant']
        
        for job_title, job_url, job_city, job_country in zip(self.job_titles, self.job_urls, self.job_cities, self.job_countries):
            if job_title in exception_jobs:
                remote = 'hybrid'
            else:
                remote = 'on-site'
                
            if job_city == "Bucharest":
                job_city = "București"
            if job_country == "Romania":
                job_country = "România"
            self.create_jobs_dict(job_title, job_url, job_country, job_city, remote)

if __name__ == "__main__":
    nielseniq = nielseniqScraper()
    nielseniq.get_response()
    nielseniq.scrape_jobs()
    nielseniq.sent_to_future()
    
    
