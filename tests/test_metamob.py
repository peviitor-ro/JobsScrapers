import pytest
from sites.metamob import metamobScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.metamob.ro/ro/companie/cariera'
        URL_LOGO = 'https://www.metamob.ro/images/1000x200_logo_metamob.png'
        company_name = 'metamob'
        metamob = metamobScrapper(company_name, URL, URL_LOGO)
        metamob.get_response()
        metamob.scrape_jobs()
        # metamob.send_to_viitor()
        
        self.scraper_data = metamob.return_data()

class Test_metamob(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('metamob', 'România')

    def test_metamob(self, get_data):
        """
        Test the metamob website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])