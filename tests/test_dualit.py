import pytest
from sites.dualit import dualitScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://dualit.ro/careers/'
        URL_LOGO = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/dualit.jpg'
        company_name = 'dualit'
        dualit = dualitScrapper(company_name, URL, URL_LOGO)
        dualit.get_response()
        dualit.scrape_jobs()
        # dualit.send_to_viitor()
        
        self.scraper_data = dualit.return_data()

class Test_dualit(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('dualit', 'România')

    def test_dualit(self, get_data):
        """
        Test the dualit website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])