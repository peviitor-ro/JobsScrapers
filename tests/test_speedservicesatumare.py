import pytest
from sites.speedservicesatumare import speedservicesatumareScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://speedservicesatumare.ro/cariere/'
        URL_LOGO = 'https://speedservicesatumare.ro/wp-content/uploads/2018/03/logo-speed-service-satu-mare.png'
        company_name = 'speedservicesatumare'
        speedservicesatumare = speedservicesatumareScrapper(company_name, URL, URL_LOGO)
        speedservicesatumare.get_response()
        speedservicesatumare.scrape_jobs()
        # speedservicesatumare.send_to_viitor()
        
        self.scraper_data = speedservicesatumare.return_data()

class Test_speedservicesatumare(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('speedservicesatumare', 'România')

    def test_speedservicesatumare(self, get_data):
        """
        Test the speedservicesatumare website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])