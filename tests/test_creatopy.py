import pytest
from sites.creatopy import CreatopyScrape
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://creatopy.bamboohr.com/careers/list'
        URL_LOGO = 'https://images4.bamboohr.com/146133/logos/cropped.jpg?v=51'
        company_name = 'Creatopy'
        Creatopy = CreatopyScrape(company_name, URL, URL_LOGO)
        Creatopy.set_headers()
        Creatopy.get_response()
        Creatopy.scrape_jobs()
        # creatopy.send_to_viitor()
        
        self.scraper_data = Creatopy.return_data()

class Test_creatopy(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('creatopy', 'România')

    def test_creatopy(self, get_data):
        """
        Test the creatopy website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])