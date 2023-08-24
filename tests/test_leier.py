import pytest
from sites.leier import leierScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.leier.ro/cariere/'
        URL_LOGO = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc0aKksxn_ZPQOnyn9-dAc9KQkWMPWwG5d7cuYX8AUgGV0xIuDqAFpt14Q7b5yNwqHGAk'
        company_name = 'leier'
        leier = leierScrapper(company_name, URL, URL_LOGO)
        leier.get_response()
        leier.scrape_jobs()
        # leier.send_to_viitor()
        
        self.scraper_data = leier.return_data()

class Test_leier(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('leier', 'România')

    def test_leier(self, get_data):
        """
        Test the leier website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])