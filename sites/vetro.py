#
#
#
#
## vetro > https://vetro.vet/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class vetroScraper(BS4Scraper):
    
    """
    A class for scraping job data from vetro website.
    """
    url = 'https://vetro.vet/cariere/'
    url_logo = 'https://vetro.vet/wp-content/uploads/2020/08/Logo_Vetro-2048x550.png'
    company_name = 'vetro'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from vetro website.
        """

        job_elements = self.get_jobs_elements('css_', 'section.elementor-section.elementor-top-section.elementor-element.elementor-element-31c883d.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > section > div > div > div > div > div > h2')
        job_urls_elements = self.get_jobs_elements('class_', 'elementor-button elementor-button-link elementor-size-sm')

        self.job_titles = self.get_jobs_details_text(job_elements)[::3]
        self.job_cities = self.get_jobs_details_text(job_elements)[1::3]
                                         
        self.job_urls = [job_url for job_url in self.get_jobs_details_href(job_urls_elements) if job_url.startswith('https://vetro.vet/cariere')]

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
        for job_title, job_city, job_url in zip(self.job_titles, self.job_cities, self.job_urls):
            if job_city == "Moldova":
                continue
            if job_city == "Bihor":
                job_city = ["Oradea","Salonta","Marghita","Beius","Valea lui Mihai","Stei","Alesd","Sacueni","Diosig","Tinca","Tileagd","Sanmartin","Vadu Crisului","Biharia","Curtuiseni","Suplacu de Barcau","Popesti","Salard","Simian","Santandrei","Tulca","Osorhei","Salacea","Rosia","Suncuius","Avram Iancu","Voivozi","Dobresti","Vascau","Ineu","Ghiorac","Finis","Tarian","Ciumeghiu","Batar","Bratca","Talpos","Nucet","Budureasa","Beznea","Nojorid","Astileu","Petreu","Borod","Lugasu de Jos","Brusturi","Pestis","Santion","Balc","Meziad","Cuzap","Saniob","Bogei","Cefa","Tasad","Calacea","Livada de Bihor","Tarcaia","Varciorog","Gurbediu","Sarbi","Girisu de Cris","Sannicolau Roman","Cadea","Burzuc","Rosiori","Mihai Bravu","Tamasda","Remeti","Luncsoara","Forau","Budoi","Tauteu","Bors","Cordau","Chet","Chesereu","Hotar","Bistra","Ianosda","Vasad","Luncasprie","Cubulcut","Hidiselu de Sus","Albis","Cociuba Mare","Derna","Balnaca","Lunca","Cabesti","Cheresig","Padurea Neagra","Cetariu","Galospetreu","Ghighiseni","Viisoara","Pietroasa","Silindru","Gepiu","Misca","Buduslau","Alparea","Vintere","Bulz","Ciutelec","Campani","Toboliu","Grosi","Tarcea","Taut","Tamaseu","Calatea","Palota","Sannicolau de Munte","Tilecus","Borumlaca","Almasu Mare","Nimaiesti","Picleu","Urvind","Ceica","Sacadat","Urvis de Beius","Madaras","Arpasel","Ciocaia","Uileacu de Cris","Mierlau","Boiu","Inand","Fughiu","Girisu Negru","Remetea","Hinchiris","Damis","Husasau de Cris","Suncuis","Abram","Cihei","Adoni","Lugasu de Sus","Ponoara","Calugari","Haieu","Balaia","Pestere","Chesa","Carasau","Cosdeni","Gurani","Cherechiu","Tinaud","Topa de Sus","Ghenetea","Chiscau","Tetchea","Otomani","Uileacu de Beius","Sacalasau","Husasau de Tinca","Chiribis","Poienii de Sus","Sabolciu","Homorog","Hidisel","Serani","Ceisoara","Fanate","Hodos","Pagaia","Bradet","Izbuc","Rapa","Petid","Valani de Pomezeu","Rabagani","Dernisoara","Calea Mare","Serghis","Seghiste","Botean","Munteni","Holod","Saldabagiu Mic","Telechiu","Ioanis","Olcea","Poienii de Jos","Orvisele","Zece Hotare","Sinteu","Borozel","Sisterea","Gepis","Soimi","Lazareni","Poiana","Boianu Mare","Chistag","Baita","Varviz","Chiraleu","Rieni","Ucuris","Roit","Dusesti","Margine","Subpiatra","Corbesti","Dobricionesti","Targusor","Cornitel","Santimreu","Ferice","Carpinet","Valea de Jos","Chislaz","Saldabagiu de Barcau","Cauaceu","Sitani","Fasca","Petrileni","Dumbravita de Codru","Vaida","Cotiglet","Saucani","Saliste de Vascau","Bicaci","Cusuius","Buntesti","Saldabagiu de Munte","Valea Crisului","Crancesti","Les","Campani de Pomezeu","Dumbrava","Olosig","Hidiselu de Jos","Sititelec","Lorau","Bucuroaia","Uileacu de Munte","Beiusele","Almasu Mic","Surduc","Valea Mare de Cris","Lupoaia","Prisaca","Voivozi","Suiug","Suplacu de Tinca","Cresuia","Spinus","Belfir","Dragoteni","Varaseni","Cheriu","Auseu","Sarand","Sustiu","Cauasd","Lelesti","Tria","Leheceni","Topa de Cris","Parhida","Pocola","Cuiesd","Hidis","Lazuri","Feneris","Sumugiu","Incesti","Tarcaita","Ortiteag","Paleu","Betfia","Abramut","Valea Tarnei","Gradinari","Osand","Burda","Capalna","Sambata","Curatele","Briheni","Hodisel","Crestur","Mizies","Ciuhoi","Sanlazar","Petreasa","Cociuba Mica","Saud","Cristioru de Jos","Josani","Paulesti","Ginta","Valea Cerului","Tomnatic","Miersig","Tiganestii de Cris","Copacel","Dragesti","Delani","Petrani","Draganesti","Sudrigiu","Sacalasau Nou","Sighistel","Valea de Sus","Poclusa de Barcau","Birtin","Albesti","Rogoz","Cetea","Sarbesti","Harsesti","Santaul Mic","Lazuri de Beius","Josani","Sohodol","Pocioveliste","Camp","Butani","Rontau","Sauaieu","Varzari","Susturogi","Magura","Fegernic","Santelec","Fancica","Hotarel","Tiganestii de Beius","Cacuciu Nou","Posoloaca","Sebis","Iteu","Dijir","Felcheriu","Dumbravani","Galaseni","Stracos","Berechiu","Totoreni","Dumbravita","Cornisesti","Belejeni","Sarsig","Valanii de Beius","Dicanesti","Saliste","Stancesti","Spinus de Pomezeu","Hodis","Varzarii de Jos","Chijic","Codru","Colesti","Santaul Mare","Borz","Cenalos","Pausa","Talpe","Magesti","Sfarnas","Zavoiu","Izvoarele","Satu Barba","Apateu","Chioag","Ianca","Saliste de Beius","Bucium","Topesti","Ciulesti","Bicacel","Gheghie","Borsa","Mierag","Fizis","Topa de Jos","Nadar","Valcelele","Balnaca-Grosi","Baleni","Satu Nou","Miheleu","Sanmartin de Beius","Tautelec","Ursad","Forosig","Ogesti","Goila","Poiana","Cristioru de Sus","Huta Voivozi","Gurbesti","Niuved","Poiana Tasad","Saca","Ant","Teleac","Dolea","Ateas","Calatani","Foglas","Fonau","Sannicolau de Beius","Rotaresti","Almasu Mic","Pomezeu","Carandeni","Martihaz","Ghida","Cacuciu Vechi","Pantasesti","Varzarii de Sus","Iteu Nou","Giulesti","Rohani","Varasau","Copaceni","Saliste de Pomezeu","Soimus","Gurbesti","Gruilung","Loranta","Bratesti","Camp-Moti","Cohani","Baita-Plai","Livada Beiusului","Chisirid","Caranzel","Valea Mare de Codru","Socet","Racas","Motesti","Poclusa de Beius","Sarcau","Poietari","Reghea","Cucuceni","Haucesti","Corboaia","Lacu Sarat","Codrisoru","Fegernicu Nou","Surducel","Balc","Huta","Rugea","Brusturi","Padureni","Baile Felix","Pacalesti"]
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    vetro = vetroScraper()
    vetro.get_response()
    vetro.scrape_jobs()
    vetro.sent_to_future()
    
    

