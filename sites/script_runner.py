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
        Run the scraper for each Python file in the sites directory, excluding the specified files.
        """
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sites')  # Ensure 'sites' folder is used
        for site in os.listdir(path):
            if site.endswith('.py') and site not in self.exclude:
                try:
                    print(f"Running: {sys.executable} {os.path.join(path, site)}")
                    subprocess.check_call([sys.executable, os.path.join(path, site)], cwd=path)  # Set cwd
                    print(f"Success scraping {site}")
                except subprocess.CalledProcessError as e:
                    print(f"Error scraping {site}: {e}")
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
        'reinest.py',  # This does not have a career's page now
        'typingdna.py',  # This does not have a career's page now
        'netrom.py',  # This does not have a career's page now
        # 'nokia.py',  # Taking too long
        'kaizengaming.py',  # Website changed
        'careerscenter.py',  # Website cannot be accessed in actions
        'brillio.py',  # there are no jobs available
        'aeroportoradea.py',  # Removed as they changed the page layout, to be fixed
        'mennekes.py',  # This does not have jobs at this moment
        'iasidelivery.py',  # Website not working
        'apavital.py',
        'qubiz.py',
        'getCounty.py',
        'test.py'
    ]

    scraper = Scraper(exclude)
    scraper.run()
