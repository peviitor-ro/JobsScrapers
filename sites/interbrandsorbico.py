#
#
#
# InterbrandsOrbico > https://interbrandsorbico.recruitee.com/oportunitati-deschise


from sites.website_scraper_bs4 import BS4Scraper
from requests_html import HTMLSession
from bs4 import BeautifulSoup


class InterbrandsOrbicoScraper(BS4Scraper):
    
    """
    A class for scraping job data from InterbrandsOrbico website.
    """
    url = 'https://interbrandsorbico.recruitee.com/oportunitati-deschise'
    url_logo = 'https://d27i7n2isjbnbi.cloudfront.net/careers/photos/270715/thumb_photo_1658741832.png'
    company_name = 'InterbrandsOrbico'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        self.session = HTMLSession()
        
    def get_response(self):
        self.session = HTMLSession()
        r = self.session.get(self.url)
        r.html.render(sleep=5, timeout=30)
        self.html_content = r.html.html
        
    def scrape_jobs(self):
        """
        Scrape job data from InterbrandsOrbico website.
        """
        soup = BeautifulSoup(self.html_content, 'lxml')
        
        self.job_titles = []
        self.job_cities = []
        self.job_urls = []
        self.job_remotes = []
        self.job_salaries = []
        
        job_cards = soup.find_all(class_='sc-6exb5d-0')
        
        for card in job_cards:
            title_elem = card.find(class_='sc-6exb5d-1')
            title = title_elem.text.strip() if title_elem else ''
            
            if not title:
                continue
            
            city_elem = card.find(class_='custom-css-style-job-location-city')
            city = city_elem.text.strip() if city_elem else ''
            
            location_elem = card.find(class_='custom-css-style-job-location')
            location_text = location_elem.text.strip() if location_elem else ''
            
            remote = 'on-site'
            salary = ''
            
            location_elems = card.find_all(class_='sc-6exb5d-4')
            for loc in location_elems:
                loc_text = loc.text.strip()
                if 'RON' in loc_text and 'per month' in loc_text:
                    salary = loc_text
                elif loc_text in ['Hybrid', 'On-site, Hybrid', 'Hybrid, On-site']:
                    remote = 'hybrid'
                elif loc_text == 'On-site':
                    remote = 'on-site'
                elif 'All around' in location_text:
                    city = 'România'
                    remote = 'on-site'
            
            view_job_link = card.find('a', href=lambda h: h and '/o/' in h)
            job_url = ''
            if view_job_link:
                href = view_job_link.get('href', '')
                if href and href.startswith('/o/'):
                    job_url = f'https://interbrandsorbico.recruitee.com{href}'
            
            city = city.replace('Bucharest', 'Bucuresti')
            
            self.job_titles.append(title)
            self.job_cities.append(city if city and city != 'România' else 'Bucuresti')
            self.job_urls.append(job_url)
            self.job_remotes.append(remote)
            self.job_salaries.append(salary)
            
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
        for job_title, job_url, job_city, job_remote, job_salary in zip(
            self.job_titles, self.job_urls, self.job_cities, self.job_remotes, self.job_salaries):
            if job_city == 'România':
                self.create_jobs_dict(job_title, job_url, "România", job_city, job_remote, job_salary)
            else:
                self.create_jobs_dict(job_title, job_url, "România", job_city, job_remote, job_salary)

    def create_jobs_dict(self, job_title, job_url, job_country, job_city, remote='on-site', salary='', county=None):
        """
        Create the job dictionary for the future api
        """
        self.counties = []
        
        if not county:
            if type(job_city) == list:
                for city in job_city:
                    self.counties.append(self.get_county(city))
                job_county = self.counties
            else:
                job_county = self.get_county(job_city) if job_city != 'România' else None
        else:
            job_county = county
                    
        job_data = {
            "job_title": job_title,
            "job_link": job_url,
            "company": self.company_name,
            "country": job_country,
            "county": job_county,
            "city": job_city,
            "remote": remote
        }
        
        if salary:
            salary_text = salary.upper()
            currency = 'RON'
            salary_cleaned = salary_text.replace('RON', '').replace('EUR', '').replace('USD', '').replace('PER MONTH', '').replace('-', ' ').strip()
            parts = salary_cleaned.split()
            try:
                parts = [p.replace(',', '').replace('.', '') for p in parts if p.replace(',', '').replace('.', '').isdigit()]
                if len(parts) >= 1:
                    job_data['salary_min'] = int(parts[0])
                if len(parts) >= 2:
                    job_data['salary_max'] = int(parts[1])
                job_data['salary_currency'] = currency
            except:
                pass
        
        self.formatted_data.append(job_data)

if __name__ == "__main__":
    InterbrandsOrbico = InterbrandsOrbicoScraper()
    InterbrandsOrbico.get_response()
    InterbrandsOrbico.scrape_jobs()
    InterbrandsOrbico.sent_to_future()
