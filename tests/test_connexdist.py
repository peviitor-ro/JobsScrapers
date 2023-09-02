import pytest
from sites.conexdist import conexdistScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.conexdist.ro/ro/cariere/'
        URL_LOGO = 'https://www.conexdist.ro/wp-content/uploads/2020/11/Asset-2.png'
        company_name = 'conexdist'
        conexdist = conexdistScrapper(company_name, URL, URL_LOGO)
        conexdist.get_response()
        conexdist.scrape_jobs()
        # connexdist.send_to_viitor()
        
        self.scraper_data = conexdist.return_data()

class Test_connexdist(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('conexdist', 'România')

    def test_connexdist(self, get_data):
        """
        Test the connexdist website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])