import pytest
from sites.consultmed import consultmedScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://consultmed.ro/consultmed-clinica-diabet-nutritie-iasi/cariere/'
        URL_LOGO = 'https://consultmed.ro/wp-content/uploads/2021/06/logo7.png'
        company_name = 'consultmed'
        consultmed = consultmedScrapper(company_name, URL, URL_LOGO)
        consultmed.get_response()
        consultmed.scrape_jobs()
        # consultmed.send_to_viitor()
        
        self.scraper_data = consultmed.return_data()

class Test_consultmed(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('consultmed', 'România')

    def test_consultmed(self, get_data):
        """
        Test the consultmed website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])