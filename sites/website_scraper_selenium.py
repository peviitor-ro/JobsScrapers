from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from sites.setup_api import UpdatePeviitorAPI
from sites.update_logo import update_logo
from sites.getCounty import get_county


# Work in progress this might change significant during the creation of the following scrappers, might need further testing and improvements
class SeleniumScraper:
    """
    A class for scraping job data from a website.
    """

    def __init__(self, company_name: str, company_logo_url: str):
        """
        Define the URL, company name for the request, and initialize the formatted data list for the scraped jobs.
        """
        self.company_name = company_name
        self.logo_url = company_logo_url
        self.formatted_data = []
        
    def driver(self):
        # Set up the service object
        service = Service(ChromeDriverManager().install())
        
        # set chromeoptions
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # Set to headless
        chrome_options.headless = True
        
        # Create the webdriver using the service object
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()

    def set_expected_wait(self):
        self.expected_wait = WebDriverWait(self.driver, 15)

    def open_website(self, url):
        self.driver.get(url)
    
    def switch_to_iframe(self, element_locator, element):
        self._get_locator_strategy(element_locator)
        # Find the iframe element
        iframe_element = self.expected_wait.until(EC.presence_of_element_located((self.locator_strategy , element)))

        # Switch to the iframe
        self.driver.switch_to.frame(iframe_element)
    
    def _get_locator_strategy(self, element_locator):
        """
        Get the locator strategy from the By class
        """
        self.locator_strategy = getattr(By, element_locator.upper())

    def get_job_details(self, element_locator, element):
        """
        Grab all the elements from the page that match the locator and the element
        """
        self._get_locator_strategy(element_locator)
        job_details = self.expected_wait.until(EC.presence_of_all_elements_located((self.locator_strategy , element)))
        return [job_detail.text for job_detail in job_details]
    
    def get_job_links(self, element_locator, element):
        """
        Grab all the links from the page that match the locator and the element
        """
        self._get_locator_strategy(element_locator)
        job_details = self.expected_wait.until(EC.presence_of_all_elements_located((self.locator_strategy , element)))
        return [job_detail.get_attribute('href') for job_detail in job_details]

    def get_page_cap(self, element_locator, element):
        self._get_locator_strategy(element_locator)
        return self.expected_wait.until(EC.presence_of_element_located((self.locator_strategy, element))).text

    def close_browser(self):
        """
        Close the browser when done
        """
        self.driver.quit()
        
    def get_county(self, city):
        return get_county(city)

    def create_jobs_dict(self, job_title, job_url, job_country, job_city, remote='on-site', county=None):
        """
        Create the job dictionary for the future api
        """
        # Define a list for counties in case there is more than one
        self.counties = []
        
        if not county:
            # Get the county using the city
            if type(job_city) == list:
                for city in job_city:
                    self.counties.append(self.get_county(city))
                job_county = self.counties
            else:
                job_county = self.get_county(job_city)
        else:
            job_county = county
                
        self.formatted_data.append({
            "job_title": job_title,
            "job_link": job_url,
            "company": self.company_name,
            "country": job_country,
            "county": job_county,
            "city": job_city,
            "remote": remote
            
        })

    def send_to_viitor(self):
        """
        Sending the scrapped jobs to the future :)
        """
        api_load = UpdatePeviitorAPI(self.company_name, self.formatted_data)
        api_load()
        update_logo(self.company_name, self.logo_url)
