from module_names import module_names
from utils import TestUtils
import importlib
import pytest

class SetupTests:
    def import_all_modules(self):

        scraper_classes = []

        # for module_name, class_name in zip(module_names, class_names):
        for module_name, class_name in module_names.items():
            try:
                module = importlib.import_module(f"sites.{module_name}")
                class_obj = getattr(module, class_name)
                scraper_classes.append(class_obj)
                print(f"Imported class {class_name} from module {module_name}")
                # You can now use class_obj for further operations
            except ModuleNotFoundError:
                print(f"Module not found: {module_name}")
            except AttributeError:
                print(f"Class not found: {class_name} in module {module_name}")
        
        return scraper_classes
    
    def get_jobs_careers(self, scraper_class):
        """
        Fixture for scraping process from the career section.
        """
        self.scraper_data = scraper_class().return_data()

class TestScrapers:
    @pytest.fixture(params=SetupTests().import_all_modules())
    def scraper_class(self, request):
        return request.param
    
    @pytest.mark.regression
    def test_scrapers(self, scraper_class):
        setup_tests = SetupTests()
        setup_tests.get_jobs_careers(scraper_class)
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        scraped_jobs_data = TestUtils.scrape_jobs(setup_tests.scraper_data[0])
        peviitor_jobs_data = TestUtils.scrape_peviitor(setup_tests.scraper_data[1], 'România')

        # Test Title
        assert sorted(scraped_jobs_data[0]) == sorted(peviitor_jobs_data[0])
        # Test job city
        assert sorted(scraped_jobs_data[1]) == sorted(peviitor_jobs_data[1])
        # Test job country
        assert sorted(scraped_jobs_data[2]) == sorted(peviitor_jobs_data[2])
        # Test job link
        assert sorted(scraped_jobs_data[3]) == sorted(peviitor_jobs_data[3])
