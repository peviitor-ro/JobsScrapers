import pytest
from sites.connectgroup import connectgroupScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.connectgroup.com/en/vacancies/roemeni%C3%AB'
        URL_LOGO = 'https://www.connectgroup.com/images/logo-connectgroup.svg'
        company_name = 'connectgroup'
        connectgroup = connectgroupScrapper(company_name, URL, URL_LOGO)
        connectgroup.get_response()
        connectgroup.scrape_jobs()
        # connectgroup.send_to_viitor()
        
        self.scraper_data = connectgroup.return_data()

class Test_connectgroup(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('connectgroup', 'România')

    def test_connectgroup(self, get_data):
        """
        Test the connectgroup website against the pe viitor data
        """
        # Test Title
        print(self.scraped_jobs_data[0])
        print(self.peviitor_jobs_data[0])
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        # assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])