import pytest
from sites.nielseniq import nielseniqScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://nielseniq.com/?s=&market=global&language=en&orderby=&order=&post_type=career_job&job_locations=romania&job_teams=&job_types='
        URL_LOGO = 'https://c.smartrecruiters.com/sr-company-images-prod-aws-dc5/5f20077aa2b8ac7a5a26cb93/c83a18a7-1926-4be1-9572-10cc0fbdc9b3/huge?r=s3-eu-central-1&_1677595339802'
        company_name = 'nielseniq'
        nielseniq = nielseniqScrapper(company_name, URL, URL_LOGO)
        nielseniq.get_response()
        nielseniq.scrape_jobs()
        # nielseniq.send_to_viitor()
        
        self.scraper_data = nielseniq.return_data()

class Test_nielseniq(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('nielseniq', 'România')

    def test_nielseniq(self, get_data):
        """
        Test the nielseniq website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])