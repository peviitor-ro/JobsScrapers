import pytest
from sites.rervest import rervestScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://rervest.ro/cariere/'
        URL_LOGO = 'https://rervest.ro/wp-content/uploads/2018/02/rervest-01.svg'
        company_name = 'rervest'
        rervest = rervestScrapper(company_name, URL, URL_LOGO)
        rervest.get_response()
        rervest.scrape_jobs()
        # rervest.send_to_viitor()
        
        self.scraper_data = rervest.return_data()

class Test_rervest(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('rervest', 'România')

    def test_rervest(self, get_data):
        """
        Test the rervest website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])