import pytest
from sites.titanmachinery import titanmachineryScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.titanmachinery.ro/en/pag/careers?page='
        URL_LOGO = 'https://www.titanmachinery.ro/images/default_image_categories.png'
        company_name = 'titanmachinery'
        titanmachinery = titanmachineryScrapper(company_name, URL, URL_LOGO)
        titanmachinery.get_response()
        titanmachinery.scrape_jobs()
        # titanmachinery.send_to_viitor()
        
        self.scraper_data = titanmachinery.return_data()

class Test_titanmachinery(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('titanmachinery', 'România')

    def test_titanmachinery(self, get_data):
        """
        Test the titanmachinery website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])