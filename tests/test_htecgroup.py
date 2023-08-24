import pytest
from sites.htecgroup import htecgroupScrape
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://api.talentlyft.com/public/jswidget/54388e55-d1d7-4bc1-ab98-41a2c4e7aea4/jobs'
        URL_LOGO = 'https://htecgroup.com/wp-content/uploads/2023/05/vectorhtec-logo.svg'
        company_name = 'htecgroup'
        htecgroup = htecgroupScrape(company_name, URL, URL_LOGO)
        htecgroup.set_params()
        htecgroup.get_response()
        htecgroup.scrape_jobs()
        # htecgroup.send_to_viitor()
        
        self.scraper_data = htecgroup.return_data()

class Test_htecgroup(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('htecgroup', 'România')

    def test_htecgroup(self, get_data):
        """
        Test the htecgroup website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])