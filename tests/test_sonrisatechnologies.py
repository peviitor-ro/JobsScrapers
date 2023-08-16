import pytest
from sites.sonrisatechnologies import sonrisatechnologiesScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.careers.sonrisa.hu/#jobs'
        URL_LOGO = 'https://images.teamtailor-cdn.com/images/s3/teamtailor-production/logotype-v3/image_uploads/fc3ad244-a68c-4d8a-a08c-93eb807f80be/original.png'
        company_name = 'sonrisatechnologies'
        sonrisatechnologies = sonrisatechnologiesScrapper(company_name, URL, URL_LOGO)
        sonrisatechnologies.get_response()
        sonrisatechnologies.scrape_jobs()
        # sonrisatechnologies.send_to_viitor()
        
        self.scraper_data = sonrisatechnologies.return_data()

class Test_sonrisatechnologies(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('sonrisatechnologies', 'România')

    def test_sonrisatechnologies(self, get_data):
        """
        Test the sonrisatechnologies website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])