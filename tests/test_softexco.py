import pytest
from sites.softexco import softexcoScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://softexco.ro/p/cariere'
        URL_LOGO = 'https://scontent.fomr1-1.fna.fbcdn.net/v/t39.30808-6/291934334_539365971112037_5557795708648591685_n.png?_nc_cat=105&cb=99be929b-59f725be&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=zRboCj7GZL4AX9PaJHC&_nc_ht=scontent.fomr1-1.fna&oh=00_AfCu4Or21onBoUnnuLNmRL1y9kIj8YY-_55833UFhIRO2w&oe=64C53BE6'
        company_name = 'softexco'
        softexco = softexcoScrapper(company_name, URL, URL_LOGO)
        softexco.get_response()
        softexco.scrape_jobs()
        self.scraper_data = softexco.return_data()

class Test_softexco(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('softexco', 'România')

    def test_softexco(self, get_data):
        """
        Test the softexco website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])