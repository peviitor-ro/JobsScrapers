import pytest
from sites.cargus import CargusScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.cargus.ro/careers-ro/'
        URL_LOGO = 'https://www.cargus.ro/wp-content/uploads/logo-cargus.png'
        company_name = 'Cargus'
        Cargus = CargusScrapper(company_name, URL, URL_LOGO)
        Cargus.get_response()
        Cargus.scrape_jobs()
        
        self.scraper_data = Cargus.return_data()
    
class Test_Cargus(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('Cargus', 'România')

    def test_cargus(self, get_data):
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