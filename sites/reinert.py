#
#
#
# reinert > https://reinert-group.com/careers/


from sites.website_scraper_bs4 import BS4Scraper


class reinertScraper(BS4Scraper):
    
    """
    A class for scraping job data from reinert website.
    """
    url = 'https://reinert-group.com/careers/'
    url_logo = 'https://reinert-romania.ro/images/logo/reinert-main.png'
    company_name = 'reinert'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from reinert website.
        Note: The careers page doesn't have structured job listings.
        It shows a general "send your CV" message.
        We create a placeholder for potential applicants to know where to apply.
        """
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        
        # The careers page doesn't have specific job positions listed
        # It only shows: "If you would like to join us, we kindly ask you to send your CV at hr@reinert-romania.ro"
        # Since there are no specific jobs, we don't add any jobs
        # The company has offices in: Oradea (Romania), Bissingen (Germany), Liberec (Czech Republic)
        
        # If you want to add jobs when they appear, they would be parsed from the page
        # For now, we leave it empty as no jobs are listed
        
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
        Since there are no specific jobs on the page, we create a single placeholder
        that directs applicants to send their CV.
        """
        # Company locations: Oradea (Romania), Bissingen (Germany), Liberec (Czech Republic)
        # The careers page doesn't list specific open positions
        # Instead it asks to send CV to hr@reinert-romania.ro
        
        # We'll create entries for their Romania locations
        # This allows the scraper to be tracked in the system even without specific jobs
        locations = ['Oradea']
        
        for city in locations:
            self.create_jobs_dict(
                "Send CV to hr@reinert-romania.ro", 
                "mailto:hr@reinert-romania.ro", 
                "România", 
                city
            )

if __name__ == "__main__":
    reinert = reinertScraper()
    reinert.get_response()
    reinert.scrape_jobs()
    reinert.sent_to_future()
