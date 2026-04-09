
class Automobil:
    __marka : str
    __model : str
    __godiste : int
    __snaga_motora : int
    __max_brzina : int
    __cena : int

    naziv_fajla = "baza_auta.txt"

    def __init__(self, marka, model, godiste, snaga_motora, max_brzina, cena = 0):
        self.__marka = marka
        self.__model = model
        self.__godiste = godiste
        self.__snaga_motora = snaga_motora
        self.__max_brzina = max_brzina
        self.__cena = cena
    
    @property
    def marka(self):
        return self.__marka
    
    @marka.setter
    def marka(self, marka):
        self.__marka = marka

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def godiste(self):
        return self.__godiste   
    @godiste.setter

    def godiste(self, godiste):
        self.__godiste = godiste

    @property
    def snaga_motora(self):
        return self.__snaga_motora
    
    @snaga_motora.setter    
    def snaga_motora(self, snaga_motora):
        self.__snaga_motora = snaga_motora
    
    @property
    def max_brzina(self):
        return self.__max_brzina
    
    @max_brzina.setter
    def max_brzina(self, max_brzina):
        self.__max_brzina = max_brzina
    
    @property
    def cena(self):
        return self.__cena
    
    @cena.setter
    def cena(self, cena):
        self.__cena = cena

    def ucitaj_automobile_iz_fajla(self, naziv_fajla):
        automobili = []

        with open(naziv_fajla, "r") as fajl:
            for linija in fajl:
                linija = linija.strip()
                delovi = linija.split(":")

                auto = Automobil(
                    delovi[0],
                    delovi[1],
                    int(delovi[2]),
                    int(delovi[3]),
                    int(delovi[4]),
                    int(delovi[5])
                )

                automobili.append(auto)

        return automobili
    
    def sacuvaj_automobil_u_fajl(self, naziv_fajla):
        fajl = open(naziv_fajla, "a")
        linija = f"{self.__marka}:{self.__model}:{self.__godiste}:{self.__snaga_motora}:{self.__max_brzina}:{self.__cena}\n"
        fajl.write(linija) 
        fajl.close()

    def pretraga_automobila_po_marki(self, marka):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)
        rezultat_pretrage = []

        for auto in automobili:
            if auto.marka.lower() == marka.lower():
                rezultat_pretrage.append(auto)

        return rezultat_pretrage

    def minimalno_godiste(self, godiste):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)
        rezultat_pretrage = []

        for auto in automobili:
            if auto.godiste >= godiste:
                rezultat_pretrage.append(auto)

        return rezultat_pretrage
    
    def minimalna_snaga_motora(self, snaga_motora):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)
        rezultat_pretrage = []

        for auto in automobili:
            if auto.snaga_motora >= snaga_motora:
                rezultat_pretrage.append(auto)

        return rezultat_pretrage
    
    def maximalna_brzina(self, max_brzina):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)
        rezultat_pretrage = []

        for auto in automobili:
            if auto.max_brzina >= max_brzina:
                rezultat_pretrage.append(auto)

        return rezultat_pretrage

    def pretraga_automobila_po_minimalnoj_ceni(self, cena):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)
        rezultat_pretrage = []

        for auto in automobili:
            if auto.cena >= cena:
                rezultat_pretrage.append(auto)

        return rezultat_pretrage

    def __str__(self):
        rez = ""

        rez += f"Marka: {self.__marka}\n"
        rez += f"Model: {self.__model}\n"
        rez += f"Godiste: {self.__godiste}\n"
        rez += f"Snaga motora: {self.__snaga_motora}\n"
        rez += f"Max brzina: {self.__max_brzina}\n"
        rez += f"Cena: {self.__cena}\n"

        return rez

class KupovinaAutomobila:
    __auto : Automobil
    
    def __init__(self):
        pass   

a1 = Automobil("Toyota", "Camry", 2020, 203, 220)

opcija = -1

while opcija != 0:
    print("=== MENI ===")
    print("1) Dodaj novi automobil")
    print("2) Pretraga automobila po marki")
    print("3) Pretraga automobila po minimalnom godištu")
    print("4) Pretraga automobila po minimalnoj snazi motora")
    print("5) Pretraga automobila po maksimalnoj brzini")
    print("6) Pretraga automobila po minimalnoj ceni")
    print("0. Izlaz")
    print("=================================\n")

    opcija = int(input("Izaberite opciju: "))

    if opcija == 1:
        marka = input("Unesite marku automobila: ")
        model = input("Unesite model automobila: ")
        godiste = int(input("Unesite godište automobila: "))
        snaga_motora = int(input("Unesite snagu motora automobila: "))
        max_brzina = int(input("Unesite maksimalnu brzinu automobila: "))
        cena = int(input("Unesite cenu automobila: "))

        novi_auto = Automobil(marka, model, godiste, snaga_motora, max_brzina, cena)
        novi_auto.sacuvaj_automobil_u_fajl(novi_auto.naziv_fajla)
    elif opcija == 2:
        marka_search = input("Unesite marku automobila: ")
        rezultat = a1.pretraga_automobila_po_marki(marka_search)

        for auto in rezultat:
            print(auto)
    elif opcija == 3:
        godiste_search = int(input("Unesite minimalno godište automobila: "))
        rezultat = a1.minimalno_godiste(godiste_search)

        for auto in rezultat:
            print(auto)
    elif opcija == 4:
        snaga_search = int(input("Unesite minimalnu snagu motora automobila: "))
        rezultat = a1.minimalna_snaga_motora(snaga_search)

        for auto in rezultat:
            print(auto)
    elif opcija == 5:
        brzina_search = int(input("Unesite minimalnu maksimalnu brzinu automobila: "))
        rezultat = a1.maximalna_brzina(brzina_search)

        for auto in rezultat:
            print(auto)
    elif opcija == 6:
        cena_search = int(input("Unesite minimalnu cenu automobila: "))
        rezultat = a1.pretraga_automobila_po_minimalnoj_ceni(cena_search)

        for auto in rezultat:
            print(auto)
    elif opcija == 0:
        print("Izlaz iz programa.")
    else:
        print("Nepoznata opcija, pokušajte ponovo.")
