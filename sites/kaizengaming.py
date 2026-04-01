#
#
#
# KaizenGaming > https://job-boards.greenhouse.io/embed/job_board?for=kaizengaming


from sites.website_scraper_bs4 import BS4Scraper
import re


class KaizenGamingScraper(BS4Scraper):
    
    """
    A class for scraping job data from KaizenGaming website.
    """
    url = 'https://job-boards.greenhouse.io/embed/job_board?for=kaizengaming'
    url_logo = 'https://kaizengaming.com/wp-content/uploads/2022/11/Logo_KaizenGaming_Colour.svg'
    company_name = 'KaizenGaming'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from KaizenGaming website.
        """
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        
        job_links = self.soup.find_all('a', href=lambda h: h and 'job-details' in h)
        
        for link in job_links:
            href = link.get('href', '')
            text = link.text.strip()
            
            if not href or not text:
                continue
            
            # Parse title and location from text
            # Format: "TitleLocation" (no space between title and location)
            # e.g., "Senior Compliance OfficerBucharest, Romania"
            
            location_match = re.search(r'([A-Z][a-z]+(?:[\s,][A-Z][a-z]+)*,\s*[A-Z][a-z]+)$', text)
            if location_match:
                location = location_match.group(1)
                title = text[:location_match.start()].strip()
            else:
                # Try another pattern - just look for Romania/Bucharest in text
                if 'Romania' in text or 'Bucharest' in text:
                    title = text.replace('Romania', '').replace('Bucharest', '').strip()
                    location = 'Bucharest' if 'Bucharest' in text else 'Romania'
                else:
                    continue
            
            # Filter for Romania only
            if 'Romania' in location or 'Bucharest' in location:
                city = location.split(',')[0].strip().replace('Bucharest', 'Bucuresti')
                
                self.job_titles.append(title)
                self.job_cities.append(city)
                self.job_urls.append(href)
        
        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    KaizenGaming = KaizenGamingScraper()
    KaizenGaming.get_response()
    KaizenGaming.scrape_jobs()
    KaizenGaming.sent_to_future()
