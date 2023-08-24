import pytest
from sites.etusoft import etusoftScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.etusoft.com/locuridemunca.html'
        URL_LOGO = 'https://www.etusoft.com/assets/img/etusoft_logo.png'
        company_name = 'etusoft'
        etusoft = etusoftScrapper(company_name, URL, URL_LOGO)
        etusoft.get_response()
        etusoft.scrape_jobs()
        # etusoft.send_to_viitor()
        
        self.scraper_data = etusoft.return_data()

class Test_etusoft(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('etusoft', 'România')

    def test_etusoft(self, get_data):
        """
        Test the etusoft website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])