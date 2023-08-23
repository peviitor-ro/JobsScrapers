import pytest
from sites.kimballelectronics import kimballelectronicsScrape
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://kei.wd1.myworkdayjobs.com/wday/cxs/kei/GlobalKimballCareers/jobs'
        URL_LOGO = 'https://www.kimballelectronics.com/images/default-source/default-album/logo97f9e1ec-d733-4299-b1b1-6cf4691c0ecc.png?sfvrsn=45be445e_2'
        company_name = 'kimballelectronics'
        kimballelectronics = kimballelectronicsScrape(company_name, URL, URL_LOGO)
        kimballelectronics.set_headers()
        kimballelectronics.set_json_data()
        kimballelectronics.get_response()
        kimballelectronics.scrape_jobs()
        # kimballelectronics.send_to_viitor()
        
        self.scraper_data = kimballelectronics.return_data()

class Test_kimballelectronics(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('kimballelectronics', 'România')

    def test_kimballelectronics(self, get_data):
        """
        Test the kimballelectronics website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])