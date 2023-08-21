import pytest
from sites.oradeatechhub import oradeatechhubScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.oradeatechhub.ro/jobs'
        URL_LOGO = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/oradeatechhub.PNG'
        company_name = 'oradeatechhub'
        oradeatechhub = oradeatechhubScrapper(company_name, URL, URL_LOGO)
        oradeatechhub.get_response()
        oradeatechhub.scrape_jobs()
        # oradeatechhub.send_to_viitor()
        
        self.scraper_data = oradeatechhub.return_data()

class Test_oradeatechhub(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('oradeatechhub', 'România')

    def test_oradeatechhub(self, get_data):
        """
        Test the oradeatechhub website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])