#
#
#
# InterbrandsOrbico > https://interbrandsorbico.recruitee.com/oportunitati-deschise


from sites.website_scraper_selenium import SeleniumScraper
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import re
import time


class InterbrandsOrbicoScraper(SeleniumScraper):
    
    """
    A class for scraping job data from InterbrandsOrbico website.
    """
    url = 'https://interbrandsorbico.recruitee.com/oportunitati-deschise'
    url_logo = 'https://d27i7n2isjbnbi.cloudfront.net/careers/photos/270715/thumb_photo_1658741832.png'
    company_name = 'InterbrandsOrbico'
    base_url = 'https://interbrandsorbico.recruitee.com'
    remote_labels = {
        'on-site': 'on-site',
        'on site': 'on-site',
        'onsite': 'on-site',
        'hybrid': 'hybrid',
        'remote': 'remote',
        'fully remote': 'remote',
    }
    salary_pattern = re.compile(
        r'RON\s*[\d.,]+(?:\s*(?:-|–|—)\s*(?:RON\s*)?[\d.,]+)?\s*per month',
        re.IGNORECASE,
    )
    
    def __init__(self):
        """
        Initialize the SeleniumScraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        self.driver()
        
    def get_response(self):
        self.open_website(self.url)
        time.sleep(5)
        self.html_content = self.driver.page_source
        
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
        
        for title, city, job_url, remote, salary in self.get_offers(soup):
            if 'All around' in city:
                city = 'România'
            
            city = city.replace('Bucharest', 'Bucuresti')
            
            self.job_titles.append(title)
            self.job_cities.append(city if city and city != 'România' else 'Bucuresti')
            self.job_urls.append(job_url)
            self.job_remotes.append(remote)
            self.job_salaries.append(salary)
            
        self.format_data()
        
    def get_offers(self, soup):
        """
        Collect the published offers, reading them from the page props first
        and falling back to the rendered job cards.
        """
        offers = self.offers_from_props(soup)
        if offers:
            return offers
        return self.offers_from_cards(soup)
    
    def offers_from_props(self, soup):
        """
        Read the offers the careers page embeds in its server rendered props.
        """
        page_props = soup.find(attrs={'data-props': True})
        if page_props is None or not page_props.get('data-props'):
            return []
        
        try:
            props = json.loads(page_props['data-props'])
            offers = props.get('appConfig', {}).get('offers') or []
        except (ValueError, AttributeError, TypeError):
            return []
        
        jobs = []
        for offer in offers:
            if offer.get('status') not in (None, 'published'):
                continue
            
            slug = offer.get('slug')
            translations = offer.get('translations') or {}
            details = (
                translations.get('en')
                or translations.get('ro')
                or next(iter(translations.values()), None)
                or {}
            )
            title = (details.get('title') or '').strip()
            if not slug or not title:
                continue
            
            if offer.get('hybrid'):
                remote = 'hybrid'
            elif offer.get('remote'):
                remote = 'remote'
            else:
                remote = 'on-site'
            
            jobs.append((
                title,
                (offer.get('city') or '').strip(),
                f'{self.base_url}/o/{slug}',
                remote,
                self.format_salary(offer.get('salary')),
            ))
        
        return jobs
    
    def offers_from_cards(self, soup):
        """
        Read the offers from the job cards rendered on the careers page.
        """
        jobs = []
        seen_urls = set()
        
        for city_elem in soup.find_all(class_='custom-css-style-job-location-city'):
            title_elem = city_elem.find_previous(
                'a', href=lambda href: href and href.startswith('/o/')
            )
            if title_elem is None:
                continue
            
            href = title_elem.get('href', '')
            if not href or href in seen_urls:
                continue
            
            card = title_elem
            while card is not None and card.find(class_='custom-css-style-job-location') is None:
                card = card.parent
            
            if card is None or not any(
                element is city_elem
                for element in card.find_all(class_='custom-css-style-job-location-city')
            ):
                continue
            
            seen_urls.add(href)
            
            remote = 'on-site'
            for span in card.find_all('span'):
                label = span.get_text(' ', strip=True).lower()
                if label in self.remote_labels:
                    remote = self.remote_labels[label]
                    break
            
            salary_match = self.salary_pattern.search(card.get_text(' ', strip=True))
            salary = salary_match.group(0).replace('\xa0', ' ') if salary_match else ''
            
            jobs.append((
                title_elem.get_text(' ', strip=True),
                city_elem.get_text(' ', strip=True),
                href if href.startswith('http') else f'{self.base_url}{href}',
                remote,
                salary,
            ))
        
        return jobs
    
    @staticmethod
    def format_salary(salary):
        """
        Build the salary text out of the offer salary details.
        """
        if not isinstance(salary, dict):
            return ''
        
        currency = salary.get('currency') or 'RON'
        values = [
            value for value in (salary.get('min'), salary.get('max'))
            if value is not None
        ]
        if not values:
            return ''
        
        salary_text = f'{currency} {int(values[0]):,}'
        if len(values) > 1:
            salary_text += f' - {currency} {int(values[1]):,}'
        
        return f'{salary_text} per month'

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
