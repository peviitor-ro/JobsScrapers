import pytest
from sites.reinert import reinertScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://reinert.ro/cariere/'
        URL_LOGO = 'https://reinert.ro/wp-content/uploads/2018/02/reinert-01.svg'
        company_name = 'reinert'
        reinert = reinertScrapper(company_name, URL, URL_LOGO)
        reinert.get_response()
        reinert.scrape_jobs()
        # reinert.send_to_viitor()
        
        self.scraper_data = reinert.return_data()

class Test_reinert(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('reinert', 'România')

    def test_reinert(self, get_data):
        """
        Test the reinert website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])