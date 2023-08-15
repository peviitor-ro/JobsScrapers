import pytest
from sites.splendor import splendorScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.splendor.ro/cariera.html'
        URL_LOGO = 'https://www.splendor.ro/webroot/img/logo/splendor_logo1.png'
        company_name = 'splendor'
        splendor = splendorScrapper(company_name, URL, URL_LOGO)
        splendor.get_response()
        splendor.scrape_jobs()
        # splendor.send_to_viitor()
        
        self.scraper_data = splendor.return_data()

class Test_splendor(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('splendor', 'România')

    def test_splendor(self, get_data):
        """
        Test the splendor website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])