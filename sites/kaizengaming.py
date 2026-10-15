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
        self.job_countries = []
        self.job_urls = []
        
        job_links = self.soup.find_all('a', href=lambda h: h and 'job-details' in h)
        
        for link in job_links:
            href = link.get('href', '')
            
            if not href:
                continue
            
            # Each listing holds two paragraphs: title and "City, Country"
            paragraphs = []
            for paragraph in link.find_all('p'):
                # "New" badges live inside the title paragraph
                for badge in paragraph.select('.tag-container'):
                    badge.decompose()
                paragraph_text = ' '.join(paragraph.text.split())
                if paragraph_text:
                    paragraphs.append(paragraph_text)
            
            if len(paragraphs) >= 2:
                title = paragraphs[0]
                location = paragraphs[-1]
            else:
                # Fallback for the old concatenated format: "TitleCity, Country"
                text = ' '.join(link.text.split())
                if not text:
                    continue
                location_match = re.search(r',[^,]*$', text)
                if not location_match:
                    continue
                location = text[location_match.start():].lstrip(',').strip()
                title = text[:location_match.start()].strip()
            
            if not title or not location:
                continue
            
            if ',' in location:
                city, _, country = location.rpartition(',')
                city = city.strip()
                country = country.strip()
            else:
                city = location.strip()
                country = ''
            
            city = city.replace('Bucharest', 'Bucuresti')
            if country == 'Romania':
                country = 'România'
            
            self.job_titles.append(title)
            self.job_cities.append(city)
            self.job_countries.append(country)
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
        for job_title, job_url, job_city, job_country in zip(self.job_titles, self.job_urls, self.job_cities, self.job_countries):
            self.create_jobs_dict(job_title, job_url, job_country, job_city)

if __name__ == "__main__":
    KaizenGaming = KaizenGamingScraper()
    KaizenGaming.get_response()
    KaizenGaming.scrape_jobs()
    KaizenGaming.sent_to_future()
