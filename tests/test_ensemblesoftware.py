import pytest
from sites.ensemblesoftware import ensemblesoftwareScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.ensemblesoftware.ro/careers/'
        URL_LOGO = 'https://www.directmm.ro/wp-content/uploads/2021/08/ensembleLogo-blue-large.png'
        company_name = 'ensemblesoftware'
        ensemblesoftware = ensemblesoftwareScrapper(company_name, URL, URL_LOGO)
        ensemblesoftware.get_response()
        ensemblesoftware.scrape_jobs()
        # ensamblesoftware.send_to_viitor()
        
        self.scraper_data = ensemblesoftware.return_data()

class Test_ensamblesoftware(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('ensemblesoftware', 'România')

    def test_ensamblesoftware(self, get_data):
        """
        Test the ensamblesoftware website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])