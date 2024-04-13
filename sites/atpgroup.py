#
#
#
# atpgroup > https://atp-group.ro/cariere/


from sites.website_scraper_bs4 import BS4Scraper

class atpgroupScraper(BS4Scraper):
    
    """
    A class for scraping job data from atpgroup website.
    """
    url = 'https://atp-group.ro/cariere/'
    url_logo = 'https://atp-group.ro/wp-content/uploads/2022/09/logo.svg'
    company_name = 'atpgroup'
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from atpgroup website.
        """

        job_elements = self.get_jobs_elements('css_', "div.elementor-element.elementor-element-63afff4.elementor-widget.elementor-widget-theme-post-title.elementor-page-title.elementor-widget-heading > div > h3 > a")
        job_location_elements = self.get_jobs_elements('class_', 'elementor-icon-list-items elementor-post-info')
        
        self.job_cities = []
        
        for city in self.get_jobs_details_text(job_location_elements):
            if city.split("Companie:")[0].replace("Locație: ", "") == '':
                self.job_cities.append("Romania")
            else:
                self.job_cities.append(city.split("Companie:")[0].replace("Locație: ", ""))
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)

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
        city_filter = {
            "Caras-Severin":["Resita","Caransebes","Bocsa","Oravita","Otelu Rosu","Moldova Veche","Anina","Baile Herculane","Moldova Noua","Steierdorf","Teregova","Mehadia","Toplet","Bozovici","Carasova","Berzovia","Dognecea","Tarnova","Verendin","Slatina-Timis","Eftimie Murgu","Glimboca","Rusca Montana","Racasdia","Obreja","Maureni","Calnic","Bautar","Berzasca","Turnu Ruieni","Borlova","Armenis","Sichevita","Rusca","Lapusnicu Mare","Bania","Ramna","Pojejena","Coronini","Liubcova","Marga","Ciclova Romana","Domasnea","Vermes","Gradinari","Valiug","Prigor","Ghertenis","Luncavita","Varciorova","Dalboset","Plugova","Bucova","Lupac","Fizes","Cornutel","Zorlentu Mare","Greoni","Petrosnita","Maru","Mehadica","Vrani","Padina Matei","Farliug","Valea Bolvasnita","Clocotici","Iablanita","Naidas","Ciudanovita","Ilova","Varadia","Sacu","Petnic","Cornea","Carbunari","Ocna de Fier","Binis","Bucosnita","Garnic","Globu Craiovei","Prilipet","Fenes","Sopotu Vechi","Sosdea","Socol","Ciresa","Doman","Ruschita","Valisoara","Moceris","Zavoi","Sasca Montana","Ticvaniu Mare","Garbovat","Cuptoare","Zlatita","Poiana","Cavaran","Comoraste","Patas","Lapusnicel","Brebu","Sfanta Elena","Brosteni","Tirol","Macesti","Ciclova Montana","Belobresca","Soceni","Parvova","Gornea","Iaz","Campia","Crusovat","23 August","Paltinis","Forotic","Voislova","Ezeris","Golet","Bradisoru de Jos","Nermed","Pecinisca","Rafnic","Ciuchici","Valea Timisului","Mercina","Zorile","Borlovenii Vechi","Bolvasnita","Doclin","Barza","Delinesti","Radimna","Jupa","Borlovenii Noi","Zervesti","Terova","Valeapai","Zagujeni","Sasca Romana","Magura","Stinapari","Sat Batran","Secu","Surducu Mare","Vraniut","Susca","Copacele","Maciova","Iam","Tincova","Vodnic","Garliste","Berliste","Matnicu Mare","Prisian","Buchin","Scaius","Prisaca","Valea Bistrei","Ilidia","Stancilova","Goruia","Var","Canicea","Rachitova","Lescovita","Cuptoare","Carnecea","Mal","Poiana Marului","Izgar","Ticvaniu Mic","Moniom","Sadova Noua","Zlagna","Divici","Slatina-Nera","Sopotu Nou","Rugi","Ciuta","Secaseni","Potoc","Milcoveni","Moldovita","Nicolint","Ohaba-Matnic","Sub Margine","Cornereva","Cornisoru","Sadova Veche","Apadia","Ersig","Globurau","Bigar","Pestere","Dalci","Duleu","Agadici","Iabalcea","Valeadeni","Petrilova","Ciortea","Bogaltin","Bogodint","Remetea-Poganici","Ravensca","Dezesti","Jitin","Pogara de Sus","Salbagelu Nou","Socolari","Putna","Sumita","Macoviste","Zbegu","Bojia","Giurgiova","Rachita","Cozla","Topla","Cozia","Valea Mare","Calina","Zanogi","Iertof","Zorlencior","Rusova Noua","Ruginosu","Camena","Negiudin","Ohabita","Garana","Marila","Valea Rachitei","Brezon","Crusovita","Izvor","Rustin","Vama Marga","Hora Mare","Carsa Rosie","Zmogotin","Lunca Florii","Rusova Veche","Lunca Zaicii","Poiana Lunga","Carsie","Parneaura","Cracu Teiului","Poneasca","Sub Plai","Valea Rosie","Zoina","Prislop","Studena","Macoviste","Pogara","Barbosu","Obita","Strugasca","Sub Crang","Barz","Gruni","Zasloane","Mesteacan","Poienile Boinei","Costis","Frasinis","Tatu","Urcu","Bazias","Borugi","Prisacina","Boina","Inelet","Ciresel","Dolina","Lucacevat","Valea Ravensca","Arsuri","Valea Minisului","Hora Mica","Zanou","Cracu Mare","Curmatura","Dristie","Cicleni","Dobraia","Valea Sichevitei","Camenita","Prislop","Resita Mica","Scarisoara","Martinovat","Preveciori","Boinita","Brebu Nou","Brestelnic","Bratova","Cracu Almaj","Streneac","Valea Orevita","Plopu","Liborajdea","Ogasu Podului","Lindenfeld","Drencova"],
            "Ilfov":["Voluntari","Buftea","Pantelimon","Popesti Leordeni","Jilava","Chitila","Otopeni","Bragadiru","Branesti","Afumati","Peris","Balotesti","Domnesti","Magurele","1 Decembrie","Mogosoaia","Cornetu","Berceni","Moara Vlasiei","Chiajna","Glina","Clinceni","Vidra","Dobroesti","Tunari","Darasti-Ilfov","Copaceni","Ciorogarla","Ciolpani","Rosu","Cretesti","Fundeni","Tanganu","Catelu","Silistea Snagovului","Cernica","Lipia","Dragomiresti-Deal","Sintesti","Buciumeni","Balaceanca","Stefanestii de Jos","Gruiu","Gradistea","Varteju","Ghermanesti","Dascalu","Darvari","Caciulati","Burias","Stefanestii de Sus","Snagov","Tancabesti","Tamasi","Piteasca","Petrachioaia","Islaz","Alunisu","Rudeni","Corbeanca","Merii Petchii","Caldararu","Olteni","Dragomiresti-Vale","Saftica","Zurbaua","Sitaru","Ciofliceni","Sindrilita","Piscu","Pasarea","Micsunestii Mari","Dudu","Nuci","Cozieni","Dumitrana","Ganeasa","Izvorani","Posta","Moara Domneasca","Santu Floresti","Teghes","Micsunestii-Moara","Gagu","Maineasca","Vanatori","Balteni","Petresti","Surlari","Ostratu","Dumbraveni","Luparia","Manolache","Balta Neagra","Pruni","Cretuleasca","Vladiceasca","Creata","Runcu","Vadu Anei","Buda","Dimieni","Odaile","Ordoreanu"],
            "Ialomița":["Slobozia","Fetesti-Gara","Urziceni","Tandarei","Fetesti","Amara","Facaeni","Cosereni","Garbovi","Manasia","Bordusani","Munteni-Buzau","Barbulesti","Cazanesti","Dridu","Jilavele","Mihail Kogalniceanu","Traian","Saveni","Scanteia","Gheorghe Doja","Grivita","Ograda","Gheorghe Lazar","Cocora","Alexeni","Grindu","Vladeni","Movilita","Condeesti","Fierbintii de Sus","Bucu","Movila","Ion Roata","Adancata","Rosiori","Milosesti","Boranesti","Suditi","Vlasca","Maia","Slobozia Noua","Axintele","Malu Rosu","Andrasesti","Barcanesti","Ciochina","Giurgeni","Marculesti","Stelnica","Bora","Moldoveni","Valea Macrisului","Luciu","Fierbinti-Targ","Colelia","Sarateni","Fierbintii de Jos","Brosteni","Cegani","Reviga","Gura Ialomitei","Rasi","Iazu","Salcioara","Perieti","Sinesti","Smirna","Buesti","Rovine","Buliga","Patru Frati","Brazii","Balaciu","Valea Ciorii","Lacusteni","Platonesti","Cosambesti","Ciulnita","Sfantu Gheorghe","Gimbasani","Dragoesti","Borduselu","Misleanu","Poiana","Butoiu","Horia","Albesti","Armasesti","Crunti","Orezu","Marsilieni","Progresu","Ciocarlia","Lilieci","Grindasi","Paltinisu","Tovarasia","Slatioarele","Dridu-Snagov","Nicolesti","Fratilesti","Malu","Rasimnicea","Murgeanca","Orboesti","Copuzu","Maltezi","Crasanii de Jos","Grecii de Jos","Stejaru","Catrunesti","Ion Ghica","Gura Vaii","Sintesti","Fundata","Mircea cel Batran","Cotorca","Barbatescu","Ivanesti","Nenisori","Bucsa","Crasanii de Sus","Piersica","Dumitresti","Bitina-Ungureni","Hagiesti","Valea Bisericii","Bitina-Pamanteni","Chiroiu-Pamanteni","Movileanca","Livedea","Hagieni","Bataluri","Retezatu","Chiroiu-Satu Nou","Chiroiu-Ungureni","Amara Noua","Boteni"],
        }
        
        regiune_sud = ['Bucuresti'] + city_filter['Ilfov'] + ['Călărași'] + city_filter['Ialomița'] + ['Constanța']
        regiune_sud_vest = ['Dolj', 'Olt', 'Vâlcea', 'Mehedinți']
        regiune_vest = ['Hunedoara', 'Alba'] + city_filter['Caras-Severin'] + ['Arad', 'Timișoara']
        
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            if "Vest" in job_title:
                job_city = regiune_vest
            elif "Sud-Vest" in job_title:
                job_city = regiune_sud_vest
            elif "Sud" in job_title:
                job_city = regiune_sud
            else:
                job_city = job_city[:-1].replace("Cluj", "Cluj-Napoca")
                
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    atpgroup = atpgroupScraper()
    atpgroup.get_response()
    atpgroup.scrape_jobs()
    atpgroup.sent_to_future()
    
    

