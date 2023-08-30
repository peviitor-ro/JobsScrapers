import pytest
from sites.duktech import duktechScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.duk-tech.com/'
        URL_LOGO = 'https://imgcdn.bestjobs.eu/cdn/el/plain/employer_logo/5c59670789be5.png'
        company_name = 'duktech'
        duktech = duktechScrapper(company_name, URL, URL_LOGO)
        duktech.get_response()
        duktech.scrape_jobs()
        # duktech.send_to_viitor()
        
        self.scraper_data = duktech.return_data()

class Test_duktech(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('duktech', 'România')

    def test_duktech(self, get_data):
        """
        Test the duktech website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])