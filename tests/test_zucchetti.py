import pytest
from sites.zucchetti import zucchettiScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.zucchettiromania.com/romania/cms/careers.html'
        URL_LOGO = 'https://www.zucchettiromania.com/romania/templates/romania/img/logo.png'
        company_name = 'zucchetti'
        zucchetti = zucchettiScrapper(company_name, URL, URL_LOGO)
        zucchetti.get_response()
        zucchetti.scrape_jobs()
        # zucchetti.send_to_viitor()
        
        self.scraper_data = zucchetti.return_data()

class Test_zucchetti(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('zucchetti', 'România')

    def test_zucchetti(self, get_data):
        """
        Test the zucchetti website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])