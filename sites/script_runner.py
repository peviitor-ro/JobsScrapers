import os
import subprocess

class Scraper:
    def __init__(self, exclude):
        """
        Initialize the Scraper class with a list of files to exclude.
        """
        self.exclude = exclude

    def run(self):
        """
        Run the scraper for each Python file in the current directory, excluding the specified files.
        """
        # Get the current directory where this script is located (should be the 'sites' directory)
        path = os.path.dirname(os.path.abspath(__file__))  # This already points to 'sites'

        # Iterate over all files in the 'sites' directory
        for site in os.listdir(path):
            if site.endswith('.py') and site not in self.exclude:
                script_path = os.path.join(path, site)
                try:
                    print(f"Running: python3 {script_path}")
                    # Run the script with 'python3' using shell=True to simulate direct execution
                    result = subprocess.run(f'python3 {script_path}', cwd=path, shell=True, check=True, env=os.environ)
                    print(f"Success scraping {site} with exit code {result.returncode}")
                except subprocess.CalledProcessError as e:
                    print(f"Error scraping {site} with exit code {e.returncode}: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred while scraping {site}: {e}")



if __name__ == "__main__":
    # exclude files
    exclude = [
        '__init__.py',
        'script_runner.py',
        'setup_api.py',
        'update_logo.py',
        'website_scraper_api.py',
        'website_scraper_bs4.py',
        'website_scraper_selenium.py',
        'reinert.py',  # This does not have a career's page now
        'typingdna.py',  # This does not have a career's page now
        # 'nokia.py',  # uncomment again if actions take too long
        'careerscenter.py',  # Website cannot be accessed in actions
        'brillio.py',  # there are no jobs available
        'aeroportoradea.py',  # Removed as they changed the page layout, to be fixed
        'iasidelivery.py',  # Website not working
        'qubiz.py',
        'getCounty.py',
        'canopy', # No jobs displayed on page currently
        'test.py'
    ]

    scraper = Scraper(exclude)
    scraper.run()
