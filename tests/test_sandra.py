import pytest
from sites.sandra import sandraScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.sandra.ro/job-uri'
        URL_LOGO = 'https://www.sandra.ro/@@poi.imageproxy/dee829ad349d413cb021a58367333415/dealer-logo.svg'
        company_name = 'sandra'
        sandra = sandraScrapper(company_name, URL, URL_LOGO)
        sandra.get_response()
        sandra.scrape_jobs()
        # sandra.send_to_viitor()
        
        self.scraper_data = sandra.return_data()

class Test_sandra(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('sandra', 'România')

    def test_sandra(self, get_data):
        """
        Test the sandra website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])