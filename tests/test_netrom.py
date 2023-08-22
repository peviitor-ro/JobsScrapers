import pytest
from sites.netrom import NetromScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.netromsoftware.ro/jobs'
        URL_LOGO = 'https://www.netromsoftware.ro/images/logo.png'
        company_name = 'Netrom'
        Netrom = NetromScrapper(company_name, URL, URL_LOGO)
        Netrom.get_response()
        Netrom.scrape_jobs()
        # netrom.send_to_viitor()
        
        self.scraper_data = Netrom.return_data()

class Test_netrom(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('Netrom', 'România')

    def test_netrom(self, get_data):
        """
        Test the netrom website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])