import pytest
from sites.kaizengaming import KaizenGamingScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://kaizengaming.com/open-positions/'
        URL_LOGO = 'https://kaizengaming.com/wp-content/uploads/2022/11/Logo_KaizenGaming_Colour.svg'
        company_name = 'KaizenGaming'
        KaizenGaming = KaizenGamingScrapper(company_name, URL, URL_LOGO)
        KaizenGaming.get_response()
        KaizenGaming.scrape_jobs()
        # kaizengaming.send_to_viitor()
        
        self.scraper_data = KaizenGaming.return_data()

class Test_kaizengaming(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('KaizenGaming', 'România')

    def test_kaizengaming(self, get_data):
        """
        Test the kaizengaming website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        # assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])