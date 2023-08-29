import pytest
from sites.iasidelivery import iasideliveryScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://iasi.delivery/cariere-horeca/'
        URL_LOGO = 'https://iasi.delivery/wp-content/uploads/2023/04/IasiDelivery_LOGO_HPositive-1.png'
        company_name = 'iasidelivery'
        iasidelivery = iasideliveryScrapper(company_name, URL, URL_LOGO)
        iasidelivery.get_response()
        iasidelivery.scrape_jobs()
        # iasidelivery.send_to_viitor()
        
        self.scraper_data = iasidelivery.return_data()

class Test_iasidelivery(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('iasidelivery', 'România')

    def test_iasidelivery(self, get_data):
        """
        Test the iasidelivery website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])