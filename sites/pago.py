#
#
#
# Pago > https://pago.ro/en/jobs


from urllib.parse import urljoin

from sites.website_scraper_bs4 import BS4Scraper


class PagoScraper(BS4Scraper):

    url = 'https://pago.ro/en/jobs'
    url_logo = 'https://besticon-demo.herokuapp.com/lettericons/P-120-6a4397.png'
    company_name = 'Pago'

    def __init__(self):
        super().__init__(self.company_name, self.url_logo)

    def get_response(self):
        self.get_content(self.url)

    def scrape_jobs(self):
        self.job_titles = []
        self.job_urls = []

        for a_tag in self.soup.find_all('a', class_='btn-secondary-outline'):
            href = a_tag.get('href', '')
            if href == 'https://revolutpeople.com/pago/public/careers':
                continue

            job_card = a_tag.find_parent('div')
            title_span = job_card.find('span', style=lambda v: 'font-weight: 700' in (v or ''))
            if title_span:
                self.job_titles.append(title_span.get_text(strip=True))
                self.job_urls.append(urljoin('https://pago.ro', href))

        self.format_data()

    def sent_to_future(self):
        self.send_to_viitor()

    def return_data(self):
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        for job_title, job_url in zip(self.job_titles, self.job_urls):
            self.create_jobs_dict(job_title, job_url, "România", "Bucuresti", "remote")


if __name__ == "__main__":
    Pago = PagoScraper()
    Pago.get_response()
    Pago.scrape_jobs()
    Pago.sent_to_future()
    
    

