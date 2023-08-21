import pytest
from sites.polipolmobila import polipolmobilaScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.polipolmobila.ro/locuri-de-munca-disponibile/'
        URL_LOGO = 'https://www.polipolmobila.ro/media/images/web/logo.png'
        company_name = 'polipolmobila'
        polipolmobila = polipolmobilaScrapper(company_name, URL, URL_LOGO)
        polipolmobila.get_response()
        polipolmobila.scrape_jobs()
        # polipolmobila.send_to_viitor()
        
        self.scraper_data = polipolmobila.return_data()

class Test_polipolmobila(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('polipolmobila', 'România')

    def test_polipolmobila(self, get_data):
        """
        Test the polipolmobila website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])