import pytest
from sites.secondtex import secondtexScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.secondtex.ro/ro/loc-de-munca'
        URL_LOGO = 'https://www.secondtex.ro/sites/all/themes/bootstrap/logo.png'
        company_name = 'secondtex'
        secondtex = secondtexScrapper(company_name, URL, URL_LOGO)
        secondtex.get_response()
        secondtex.scrape_jobs()
        # secondtex.send_to_viitor()
        
        self.scraper_data = secondtex.return_data()

class Test_secondtex(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('secondtex', 'România')

    def test_secondtex(self, get_data):
        """
        Test the secondtex website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])