from module_names import module_names
from utils import TestUtils
import importlib
import pytest
import allure

class SetupTests:
    def import_all_modules(self):
        """
        Import all scraper modules specified in module_names.
        """
        
        scraper_classes = []

        for module_name, class_name in module_names.items():
            try:
                module = importlib.import_module(f"sites.{module_name}")
                class_obj = getattr(module, class_name)
                scraper_classes.append(class_obj)
                print(f"Imported class {class_name} from module {module_name}")
            except ModuleNotFoundError:
                print(f"Module not found: {module_name}")
            except AttributeError:
                print(f"Class not found: {class_name} in module {module_name}")

        return scraper_classes

    def get_jobs_careers(self, scraper_class):
        """
        Get job data using the provided scraper class.
        """
        self.scraper_data = scraper_class().return_data()
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data[0])
        self.peviitor_jobs_data = TestUtils.scrape_peviitor(self.scraper_data[1], 'România')

@pytest.fixture(params=SetupTests().import_all_modules(), scope="class")
def scraper_class(request):
    """Fixture for providing different scraper classes as parameters."""
    return request.param

@pytest.fixture(scope="class")
def setup_tests(scraper_class):
    """
    Fixture for setting up tests with the provided scraper class.
    """
    setup_tests_instance = SetupTests()
    setup_tests_instance.get_jobs_careers(scraper_class)
    return setup_tests_instance

class TestScrapers:

    @pytest.mark.regression
    @pytest.mark.API
    def test_scrapers_title(self, setup_tests):
        
        # Dynamically set the title with the company name
        company_name = setup_tests.scraper_data[1]
        allure.dynamic.title(f"Validate job titles from the {company_name} website against Peviitor API Response")

        with allure.step("Step 1: Get job titles from the scraper"):
            job_titles_scraper = sorted(setup_tests.scraped_jobs_data[0])
        
        with allure.step("Step 2: Get job titles from the Peviitor API"):
            job_titles_peviitor = sorted(setup_tests.peviitor_jobs_data[0])
        
        missing_job_titles = []
        # Itterate over job titles and if not present on peviitor add to missing job title list
        for job_title in job_titles_scraper:
            if job_title not in job_titles_peviitor:
                missing_job_titles.append(job_title)
        
        with allure.step("Step 3: Compare job titles from scraper response against Peviitor API Response"):
            # If the missing job list is empty it might mean there are more jobs on peviitor than needed
            if missing_job_titles == []:
                missing_job_titles_peviitor = []
                for job_title in job_titles_peviitor:
                    if job_title not in job_titles_scraper:
                        missing_job_titles_peviitor.append(job_title)
                        
                # If there are way too many jobs titles only list a couple of them
                if len(missing_job_titles_peviitor) > 20:
                    missing_job_titles_peviitor = f"{missing_job_titles_peviitor[:5]} and many more"
                                
                print(f"Expected Results: {job_titles_scraper}\n")
                print(f"Actual Results: {job_titles_peviitor}")
                assert job_titles_scraper == job_titles_peviitor, f"Peviitor is having the following extra jobs titles: {missing_job_titles_peviitor}\n\n"
            else:
                if len(missing_job_titles) > 20:
                    missing_job_titles = f"{missing_job_titles[:5]} and many more"
                    
                print(f"Expected Results: {job_titles_scraper}\n")
                print(f"Actual Results: {job_titles_peviitor}")
                assert job_titles_scraper == job_titles_peviitor, f"Peviitor is missing the following job titles: {missing_job_titles}\n\n"
                

    @pytest.mark.regression
    @pytest.mark.API
    def test_scrapers_city(self, setup_tests):
        
        # Dynamically set the title with the company name
        company_name = setup_tests.scraper_data[1]
        allure.dynamic.title(f"Validate job cities from the {company_name} website against Peviitor API Response")
        
        with allure.step("Step 1: Get job cities from the scraper"):
            job_cities_scraper = sorted(setup_tests.scraped_jobs_data[1])
        
        with allure.step("Step 2: Get job cities from the Peviitor API"):
            job_cities_peviitor = sorted(setup_tests.peviitor_jobs_data[1])
        
        with allure.step("Step 3: Compare job cities from scraper response against Peviitor API Response"):
            print(f"Expected Results: {job_cities_scraper}\n")
            print(f"Actual Results: {job_cities_peviitor}")
            
            if job_cities_scraper != job_cities_peviitor:
                assert job_cities_scraper == job_cities_peviitor, f"Peviitor is having extra jobs cities\n\n"
            else:
                assert job_cities_scraper == job_cities_peviitor, f"Peviitor is missing job cities\n\n"
                
    @pytest.mark.regression
    @pytest.mark.API
    def test_scrapers_country(self, setup_tests):
        
        # Dynamically set the title with the company name
        company_name = setup_tests.scraper_data[1]
        allure.dynamic.title(f"Validate job countries from the {company_name} website against Peviitor API Response")
        
        with allure.step("Step 1: Get job countries from the scraper"):
            job_countries_scraper = sorted(setup_tests.scraped_jobs_data[2])
        
        with allure.step("Step 2: Get job countries from the Peviitor API"):
            job_countries_peviitor = sorted(setup_tests.peviitor_jobs_data[2])
        
        with allure.step("Step 3: Compare job countries from scraper response against Peviitor API Response"):
            print(f"Expected Results: {job_countries_scraper}\n")
            print(f"Actual Results: {job_countries_peviitor}")
            if job_countries_scraper != job_countries_peviitor:
                assert job_countries_scraper == job_countries_peviitor, f"Peviitor is having extra job countries\n\n"
            else:
                assert job_countries_scraper == job_countries_peviitor, f"Peviitor is missing job countries\n\n"

    @pytest.mark.regression
    @pytest.mark.API
    def test_scrapers_link(self, setup_tests):
        
        # Dynamically set the title with the company name
        company_name = setup_tests.scraper_data[1]
        allure.dynamic.title(f"Validate job links from the {company_name} website against Peviitor API Response")
        
        with allure.step("Step 1: Get job links from the scraper"):
            job_links_scraper = sorted(setup_tests.scraped_jobs_data[3])
        
        with allure.step("Step 2: Get job links from the Peviitor API"):
            job_links_peviitor = sorted(setup_tests.peviitor_jobs_data[3])
        
        missing_job_links = []
        
        for job_link in job_links_scraper:
            if job_link not in job_links_peviitor:
                missing_job_links.append(job_link)
        
        with allure.step("Step 3: Compare job links from scraper response against Peviitor API Response"):
            print(f"Expected Results: {job_links_scraper}\n")
            print(f"Actual Results: {job_links_peviitor}")
            if missing_job_links == []:
                missing_job_links_peviitor = []
                if job_link in job_links_peviitor:
                    if job_link not in job_links_scraper:
                        missing_job_links_peviitor.append(job_link)
                        
                if len(missing_job_links_peviitor) > 20:
                    missing_job_links_peviitor = f"{missing_job_links_peviitor[:5]} and many more"
                assert job_links_scraper == job_links_peviitor, f"Peviitor is having the following extra jobs links: {missing_job_links_peviitor}\n\n"
            else:
                if len(missing_job_links) > 20:
                    missing_job_links = f"{missing_job_links[:5]} and many more"
                assert job_links_scraper == job_links_peviitor, f"Peviitor is missing the following job links: {missing_job_links}\n\n"
            
