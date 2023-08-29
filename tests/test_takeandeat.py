import pytest
from sites.takeandeat import takeandeatScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://takeandeat.ro/cariere/'
        URL_LOGO = 'https://static.takeaway.com/images/restaurants/ro/N55QQ3Q/logo_465x320.png'
        company_name = 'takeandeat'
        takeandeat = takeandeatScrapper(company_name, URL, URL_LOGO)
        takeandeat.get_response()
        takeandeat.scrape_jobs()
        # takeandeat.send_to_viitor()
        
        self.scraper_data = takeandeat.return_data()

class Test_takeandeat(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('takeandeat', 'România')

    def test_takeandeat(self, get_data):
        """
        Test the takeandeat website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])