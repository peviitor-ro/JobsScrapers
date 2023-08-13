import pytest
from sites.sephora import sephoraScrape
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.inside-sephora.com/api/proxy/sap/search'
        URL_LOGO = 'https://bucurestimall.ro/wp-content/uploads/2016/12/sephora_logo_1024x.png'
        company_name = 'sephora'
        sephora = sephoraScrape(company_name, URL, URL_LOGO)
        sephora.set_headers()
        sephora.set_params()
        sephora.get_response()
        sephora.scrape_jobs()
        # sephora.send_to_viitor()
        
        self.scraper_data = sephora.return_data()

class Test_sephora(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('sephora', 'România')

    def test_sephora(self, get_data):
        """
        Test the sephora website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])