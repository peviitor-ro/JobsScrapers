import pytest
from sites.signaliduna import signalidunaScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.signal-iduna.ro/cariere'
        URL_LOGO = 'https://www.signal-iduna.ro/images/og_image_v1.jpg'
        company_name = 'signaliduna'
        signaliduna = signalidunaScrapper(company_name, URL, URL_LOGO)
        signaliduna.get_response()
        signaliduna.scrape_jobs()
        self.scraper_data = signaliduna.return_data()

class Test_signaliduna(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('signaliduna', 'România')

    def test_signaliduna(self, get_data):
        """
        Test the signaliduna website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])