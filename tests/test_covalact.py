import pytest
from sites.covalact import covalactScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://covalact.ro/cariere'
        URL_LOGO = 'https://covalact.ro/static/new/images/covalact.png'
        company_name = 'covalact'
        covalact = covalactScrapper(company_name, URL, URL_LOGO)
        covalact.get_response()
        covalact.scrape_jobs()
        # covalact.send_to_viitor()
        
        self.scraper_data = covalact.return_data()

class Test_covalact(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('covalact', 'România')

    def test_covalact(self, get_data):
        """
        Test the covalact website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])