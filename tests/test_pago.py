import pytest
from sites.pago import PagoScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://pago.ro/#section-13'
        URL_LOGO = 'https://besticon-demo.herokuapp.com/lettericons/P-120-6a4397.png'
        self.company_name = 'Pago'
        Pago = PagoScrapper(self.company_name, URL, URL_LOGO)
        Pago.get_response()
        Pago.scrape_jobs()
        self.scraper_data = Pago.return_data()

class Test_pago(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('Pago', 'România')

    def test_pago(self, get_data):
        """
        Test the pago website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])