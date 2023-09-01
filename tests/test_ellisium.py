import pytest
from sites.ellisium import ellisiumScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://ellisium.ro/cariere/'
        URL_LOGO = 'https://ellisium.ro/wp-content/uploads/2022/08/Ellisium-vertical@4x-2048x1441.png.webp'
        company_name = 'ellisium'
        ellisium = ellisiumScrapper(company_name, URL, URL_LOGO)
        ellisium.get_response()
        ellisium.scrape_jobs()
        # ellisium.send_to_viitor()
        
        self.scraper_data = ellisium.return_data()

class Test_ellisium(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('ellisium', 'România')

    def test_ellisium(self, get_data):
        """
        Test the ellisium website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])