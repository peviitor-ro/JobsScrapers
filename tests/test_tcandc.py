import pytest
from sites.tcandc import tcandcScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.tcandc.com/company/career.html'
        URL_LOGO = 'https://www.tcandc.com/templates/tcandc2020/images/tcandc-header-logo_light-2022_30y.png'
        company_name = 'tcandc'
        tcandc = tcandcScrapper(company_name, URL, URL_LOGO)
        tcandc.get_response()
        tcandc.scrape_jobs()
        # tcandc.send_to_viitor()
        
        self.scraper_data = tcandc.return_data()

class Test_tcandc(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('tcandc', 'România')

    def test_tcandc(self, get_data):
        """
        Test the tcandc website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])