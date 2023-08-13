import pytest
from sites.nokia import nokiaScrape
from utils import TestUtils
import requests

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://careers.nokia.com/ajax/content/job_results'
        URL_LOGO = 'https://www.nokia.com/nokia-ro/assets/images/layout_global/Forvianokia_Logo.svg'
        company_name = 'nokia'
        nokia = nokiaScrape(company_name, URL, URL_LOGO)
        nokia.set_headers()
        nokia.set_cookies()
        nokia.post_response()
        nokia.scrape_jobs()
        # nokia.send_to_viitor()
        
        self.scraper_data = nokia.return_data()

class Test_nokia(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('nokia', 'România')

    def test_nokia(self, get_data):
        """
        Test the nokia website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])