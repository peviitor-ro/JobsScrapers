import pytest
from sites.trencadis import trencadisScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://trencadis.ro/cariere.html'
        URL_LOGO = 'https://i0.1616.ro/media/2/2621/33206/21112260/2/trencadis.jpg?width=514'
        company_name = 'trencadis'
        trencadis = trencadisScrapper(company_name, URL, URL_LOGO)
        trencadis.get_response()
        trencadis.scrape_jobs()
        # trencadis.send_to_viitor()
        
        self.scraper_data = trencadis.return_data()

class Test_trencadis(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('trencadis', 'România')

    def test_trencadis(self, get_data):
        """
        Test the trencadis website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])