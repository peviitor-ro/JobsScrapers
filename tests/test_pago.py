import pytest
from sites.pago import PagoScrapper
from sites.website_scraper_bs4 import BS4Scraper
import requests

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://pago.ro/#section-13'
        URL_LOGO = 'https://besticon-demo.herokuapp.com/lettericons/P-120-6a4397.png'
        self.company_name = 'Pago'
        Pago = PagoScrapper(self.company_name, URL, URL_LOGO)
        Pago.get_response()
        Pago.scrape_jobs()
        self.scraper_data = Pago.return_data()
    
    def scrape_jobs(self):
        """
        Get the job details from the scrapped page
        """
        title = [title['job_title'] for title in self.scraper_data]
        job_city = [city['city'] for city in self.scraper_data]
        job_country = [country['country'] for country in self.scraper_data]
        job_link = [job_link['job_link'] for job_link in self.scraper_data]
        
        return title, job_city, job_country, job_link

    def set_params(self):
        """
        Setting params for peviitor jobs request
        """
        self.params = {
        'q': 'Pago',
        'country': 'România',
        'page': '1',
        }
    
    def get_request(self):
        """
        Send a get request to get the jobs from future
        """
        
        self.response = requests.get('https://api.peviitor.ro/v3/search/', params=self.params).json()['response']['docs']

    def scrape_peviitor(self):
        """
        Get the job details from the peviitor
        """
        future_title = [title['job_title'][0] for title in self.response]
        future_job_city = [city['city'][0] for city in self.response]
        future_job_country = [country['country'][0] for country in self.response]
        future_job_link = [job_link['job_link'][0] for job_link in self.response]
        
        return future_title, future_job_city, future_job_country, future_job_link

class Test_pago(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.set_params()
        self.get_request()
        self.get_jobs_careers()
        self.scraped_jobs_data = self.scrape_jobs()
        self.peviitor_jobs_data = self.scrape_peviitor()

    def test_pago(self, get_data):
        """
        Test the pago website against the pe viitor data
        """
        # Test Title
        assert self.scraped_jobs_data[0] == self.peviitor_jobs_data[0]
        # Test job city
        assert self.scraped_jobs_data[1] == self.peviitor_jobs_data[1]
        # Test job country
        assert self.scraped_jobs_data[2] == self.peviitor_jobs_data[2]
        # Test job link
        assert self.scraped_jobs_data[3] == self.peviitor_jobs_data[3]