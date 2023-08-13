import pytest
from sites.InterbrandsOrbico import InterbrandsOrbicoScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://interbrandsorbico.recruitee.com/#section-72572'
        URL_LOGO = 'https://d27i7n2isjbnbi.cloudfront.net/careers/photos/270715/thumb_photo_1658741832.png'
        company_name = 'InterbrandsOrbico'
        InterbrandsOrbico = InterbrandsOrbicoScrapper(company_name, URL, URL_LOGO)
        InterbrandsOrbico.get_response()
        InterbrandsOrbico.scrape_jobs()
        # InterbrandsOrbico.send_to_viitor()
        
        self.scraper_data = InterbrandsOrbico.return_data()

class Test_InterbrandsOrbico(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('InterbrandsOrbico', 'România')

    def test_InterbrandsOrbico(self, get_data):
        """
        Test the InterbrandsOrbico website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        # assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])