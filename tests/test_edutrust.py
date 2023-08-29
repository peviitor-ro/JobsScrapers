import pytest
from sites.edutrust import edutrustScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.edutrust.ro/cariera/#open-positions'
        URL_LOGO = 'https://www.edutrust.ro/wp-content/themes/yootheme/cache/39/logo-edutrust-39288933.webp'
        company_name = 'edutrust'
        edutrust = edutrustScrapper(company_name, URL, URL_LOGO)
        edutrust.get_response()
        edutrust.scrape_jobs()
        # edutrust.send_to_viitor()
        
        self.scraper_data = edutrust.return_data()

class Test_edutrust(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('edutrust', 'România')

    def test_edutrust(self, get_data):
        """
        Test the edutrust website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])