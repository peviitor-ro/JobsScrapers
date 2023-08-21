import pytest
from sites.rdnautomatic import rdnautomaticScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.rndautomatic.com/en/Career.html'
        URL_LOGO = 'https://www.rndautomatic.com/images/logo/rndlogo.png'
        company_name = 'rdnautomatic'
        rdnautomatic = rdnautomaticScrapper(company_name, URL, URL_LOGO)
        rdnautomatic.get_response()
        rdnautomatic.scrape_jobs()
        # rdnautomatic.send_to_viitor()
        
        self.scraper_data = rdnautomatic.return_data()

class Test_rdnautomatic(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('rdnautomatic', 'România')

    def test_rdnautomatic(self, get_data):
        """
        Test the rdnautomatic website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])