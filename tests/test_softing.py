import pytest
from sites.softing import softingScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://career.softing.com/open-positions/job-opportunities/softing-romania.html'
        URL_LOGO = 'https://career.softing.com/typo3conf/ext/softingtheme/Resources/Public/Images/logo.png'
        company_name = 'softing'
        softing = softingScrapper(company_name, URL, URL_LOGO)
        softing.get_response()
        softing.scrape_jobs()
        self.scraper_data = softing.return_data()

class Test_softing(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('softing', 'România')

    def test_softing(self, get_data):
        """
        Test the softing website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])