#
#
#
# kimballelectronics > https://kei.wd1.myworkdayjobs.com/GlobalKimballCareers?locations=fbecff70217d10da6c755135d69d6c29

import requests
from sites.website_scraper_api import WebsiteScraperAPI


class kimballelectronicsScraper(WebsiteScraperAPI):

    """
    A class for scraping job data from kimballelectronics website.
    """
    url = 'https://kei.wd1.myworkdayjobs.com/wday/cxs/kei/GlobalKimballCareers/jobs'
    url_logo = 'https://www.kimballelectronics.com/images/default-source/default-album/logo97f9e1ec-d733-4299-b1b1-6cf4691c0ecc.png?sfvrsn=45be445e_2'
    company_name = 'kimballelectronics'

    def __init__(self):
        """
        Initialize the WebsitescraperAPI class.
        """
        super().__init__(self.company_name, self.url, self.url_logo)

    def set_headers(self):
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        }

    def set_json_data(self):
        self.json_data = {
            'appliedFacets': {
                'locations': [
                    'fbecff70217d10da6c755135d69d6c29',
                ],
            },
            'limit': 20,
            'offset': 0,
            'searchText': '',
        }

    def get_response(self):
        """
        Send a POST request and retrieve the jobs response.
        """
        response = requests.post(self.URL, headers=self.headers, json=self.json_data, timeout=600, allow_redirects=False)

        # Check for maintenance mode redirects
        if response.status_code in (302, 303, 307, 308):
            location = response.headers.get('Location', '')
            if 'maintenance' in location.lower() or 'community.workday.com' in location:
                print(f"Warning: Kimball Electronics Workday site is in maintenance mode. Skipping scrape.")
                self.job_details = []
                self.get_jobs_response(self.job_details)
                return

        response.raise_for_status()

        content_type = response.headers.get('Content-Type', '')
        if 'application/json' not in content_type:
            print(f"Warning: API returned non-JSON response (Content-Type: {content_type}). Site may be in maintenance.")
            self.job_details = []
            self.get_jobs_response(self.job_details)
            return

        data = response.json()
        if 'jobPostings' not in data:
            print(f"Warning: Unexpected API response structure. Returning empty results.")
            self.job_details = []
            self.get_jobs_response(self.job_details)
            return

        self.job_details = data['jobPostings']
        self.get_jobs_response(self.job_details)

    def scrape_jobs(self):
        """
        Scrape job data from kimballelectronics website.
        """
        if not self.job_details:
            return

        self.job_titles = self.get_job_details(['title'])
        self.job_urls = self.get_job_details(['externalPath'])
        self.format_data()

    def sent_to_future(self):
        if self.formatted_data:
            self.send_to_viitor()
        else:
            print("No jobs to send to API.")

    def return_data(self):
        self.set_headers()
        self.set_json_data()
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            job_url = f"https://kei.wd1.myworkdayjobs.com/en-US/GlobalKimballCareers{job_url}"
            self.create_jobs_dict(job_title, job_url, "România", "Timisoara")


if __name__ == "__main__":
    kimballelectronics = kimballelectronicsScraper()
    try:
        kimballelectronics.set_headers()
        kimballelectronics.set_json_data()
        kimballelectronics.get_response()
        kimballelectronics.scrape_jobs()
        kimballelectronics.sent_to_future()
    except Exception as e:
        print(f"Scraper error: {e}")
