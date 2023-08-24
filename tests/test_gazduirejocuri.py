import pytest
from sites.gazduirejocuri import GazduireJocuriScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.gazduirejocuri.ro/cariere/'
        URL_LOGO = 'https://www.gazduirejocuri.ro/img/logo-orange.svg'
        company_name = 'GazduireJocuri'
        GazduireJocuri = GazduireJocuriScrapper(company_name, URL, URL_LOGO)
        GazduireJocuri.get_response()
        GazduireJocuri.scrape_jobs()
        # gazduirejocuri.send_to_viitor()
        
        self.scraper_data = GazduireJocuri.return_data()

class Test_gazduirejocuri(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('gazduirejocuri', 'România')

    def test_gazduirejocuri(self, get_data):
        """
        Test the gazduirejocuri website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])