import pytest
from sites.nagarro import NagarroScrape
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://hiringautomation.table.core.windows.net/CareerSiteDim?sv=2019-02-02&se=2099-10-13T20%3A47%3A00Z&sp=r&sig=%2FTWLo6vw7gzgOiS9b5wchECIjqFaaaIPV8Rs55P0W98%3D&tn=CareerSiteDim&$select=Expertise,Job_Title,Job_City,Job_Country,Level_name,Value,Job_Url,Is_job_remote_friendly,is_multiple_experience_required,RowKey&$filter=Job_Country%20eq%20%27Romania%27'
        URL_LOGO = 'https://www.nagarro.com/hubfs/NagarroWebsiteRedesign-Aug2020/Assets/Images/Nagarro%20green%20logo%20with%20title_opt.svg'
        company_name = 'Nagarro'
        Nagarro = NagarroScrape(company_name, URL, URL_LOGO)
        Nagarro.request_headers()
        Nagarro.get_response()
        # nagarro.send_to_viitor()
        
        self.scraper_data = Nagarro.return_data()

class Test_nagarro(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('nagarro', 'România')

    def test_nagarro(self, get_data):
        """
        Test the nagarro website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])