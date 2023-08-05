#
#
#
# careerscenter > https://www.careerscenter.ro/jobs/

from website_scraper_bs4 import BS4Scraper

class careerscenterScrapper(BS4Scraper):
    
    """
    A class for scraping job data from careerscenter website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        super().__init__(company_name, company_logo_url)
        
    # def get_response(self):
    #     self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from careerscenter website.
        """
        current_page = 1
        self.get_content(f"{self.url}{current_page}")
        
        self.job_titles = []
        self.job_cities = [] 
        self.job_urls = []
        
        # Get the jobs
        job_elements = self.get_jobs_elements('css_', "article[id^='post-']:not([data-expired='expirat'])")
        job_links_elements = self.get_jobs_elements('css_', "div.jobs-content-holder.eq-jobs > div > h2 > a")
        # Set the error message that will indicate inexistant page
        error_msg = self.get_jobs_details_text(self.get_jobs_elements('css_', "#post-404 > h2 > a"))
        
        
        
        while error_msg != ['Vă întoarceţi la prima pagină?']:
            
            # Remove useless data from title element and get only valid titles
            unformatted_job_titles = self.get_jobs_details_text(job_elements)
            for unformatted_job_title in unformatted_job_titles:
                self.job_titles.append(unformatted_job_title.split("Full time")[0][:-1])
                self.job_cities.append(unformatted_job_title.split("Full time")[1][1:].split()[0].replace(",", ""))
                
            # Get only the links that are in the title
            unfiltered_job_links = self.get_jobs_details_href(job_links_elements)
            unfiltered_job_links_names = self.get_jobs_details_text(job_links_elements)
            for unfiltered_job_links_name, unfiltered_job_link in zip(unfiltered_job_links_names, unfiltered_job_links):
                
                if unfiltered_job_links_name in self.job_titles:
                    self.job_urls.append(unfiltered_job_link)
            
    

            current_page += 1
            self.get_content(f"{self.url}{current_page}")
            
            error_msg = self.get_jobs_details_text(self.get_jobs_elements('css_', "#post-404 > h2 > a"))
            
            job_elements = self.get_jobs_elements('css_', "article[id^='post-']:not([data-expired='expirat'])")
            job_links_elements = self.get_jobs_elements('css_', "div.jobs-content-holder.eq-jobs > div > h2 > a")

        self.format_data()

    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "Romania", job_city)

if __name__ == "__main__":
    URL = 'https://www.careerscenter.ro/jobs/page/'
    URL_LOGO = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/careerscenter1.PNG'
    company_name = 'careerscenter'
    careerscenter = careerscenterScrapper(company_name, URL, URL_LOGO)
    careerscenter.scrape_jobs()
    careerscenter.send_to_viitor()
    
    

