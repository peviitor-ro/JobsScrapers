import pytest
from sites.nolimits import NolimitsScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.nolimits.ro/cariere.html'
        URL_LOGO = 'https://raw.githubusercontent.com/peviitor-ro/firme-peviitor/main/assets/nolimits.PNG'
        company_name = 'Nolimits'
        Nolimits = NolimitsScrapper(company_name, URL, URL_LOGO)
        Nolimits.get_response()
        Nolimits.scrape_jobs()
        # nolimits.send_to_viitor()
        
        self.scraper_data = Nolimits.return_data()

class Test_nolimits(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('nolimits', 'România')

    def test_nolimits(self, get_data):
        """
        Test the nolimits website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])