import os
# UVEZENI MODUL
import biblioteka as bib


class Automobil:
    __marka: str
    __model: str
    __godiste: int
    __snaga_motora: int
    __max_brzina: int
    __cena: int
    __id: int

    naziv_fajla = "baza_auta.txt"

    def __init__(self, marka, model, godiste, snaga_motora, max_brzina, cena=0, id=0):
        self.__marka = marka
        self.__model = model
        self.__godiste = godiste
        self.__snaga_motora = snaga_motora
        self.__max_brzina = max_brzina
        self.__cena = cena
        self.__id = id

    @property
    def marka(self):
        return self.__marka

    @property
    def model(self):
        return self.__model

    @property
    def godiste(self):
        return self.__godiste

    @property
    def snaga_motora(self):
        return self.__snaga_motora

    @property
    def max_brzina(self):
        return self.__max_brzina

    @property
    def cena(self):
        return self.__cena

    @property
    def id(self):
        return self.__id
    
    @marka.setter
    def marka(self, nova_vrednost):
        self.__marka = nova_vrednost
    
    @model.setter
    def model(self, nova_vrednost):
        self.__model = nova_vrednost
    
    @godiste.setter
    def godiste(self, nova_vrednost):
        self.__model = nova_vrednost
        
    @snaga_motora.setter
    def snaga_motora(self, nova_vrednost):
        self.__snaga_motora = nova_vrednost
    
    @max_brzina.setter
    def max_brzina(self, nova_vrednost):
        self.__max_brzina = nova_vrednost
    
    @cena.setter
    def cena(self, nova_vrednost):
        self.__cena = nova_vrednost
    
    @id.setter
    def id(self, nova_vrednost):
        self.__id = nova_vrednost

    def ucitaj_automobile_iz_fajla(self, naziv_fajla):
        automobili = []

        try:
            with open(naziv_fajla, "r", encoding="utf-8") as fajl:
                for linija in fajl:
                    linija = linija.strip()

                    if linija == "":
                        continue

                    delovi = linija.split(":")

                    auto = Automobil(
                        delovi[1],
                        delovi[2],
                        int(delovi[3]),
                        int(delovi[4]),
                        int(delovi[5]),
                        int(delovi[6]),
                        int(delovi[0])
                    )

                    automobili.append(auto)

        except FileNotFoundError:
            print("Fajl ne postoji.")

        return automobili

    def sacuvaj_automobil_u_fajl(self, naziv_fajla):
        fajl = open(naziv_fajla, "a", encoding="utf-8")

        linija = str(self.__id) + ":" + self.__marka + ":" + self.__model + ":" + str(self.__godiste) + ":" + str(self.__snaga_motora) + ":" + str(self.__max_brzina) + ":" + str(self.__cena) + "\n"

        fajl.write(linija)
        fajl.close()

    def sacuvaj_sve_automobile_u_fajl(self, automobili, naziv_fajla):
        fajl = open(naziv_fajla, "w", encoding="utf-8")

        for auto in automobili:
            linija = str(auto.id) + ":" + auto.marka + ":" + auto.model + ":" + str(auto.godiste) + ":" + str(auto.snaga_motora) + ":" + str(auto.max_brzina) + ":" + str(auto.cena) + "\n"
            fajl.write(linija)

        fajl.close()

    def obrisi_automobil_iz_fajla(self, id, naziv_fajla):
        automobili = self.ucitaj_automobile_iz_fajla(naziv_fajla)

        nova_lista = []

        for auto in automobili:
            if auto.id != id:
                nova_lista.append(auto)

        self.sacuvaj_sve_automobile_u_fajl(nova_lista, naziv_fajla)

    def pretraga_automobila_po_marki(self, marka):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)

        rezultat = []

        for auto in automobili:
            if auto.marka.lower() == marka.lower():
                rezultat.append(auto)

        return rezultat

    def minimalno_godiste(self, godiste):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)

        rezultat = []
        if godiste > 0:
            for auto in automobili:
                if auto.godiste >= godiste:
                    rezultat.append(auto)

        return rezultat

    def minimalna_snaga_motora(self, snaga):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)

        rezultat = []
        if snaga  > 0:
            for auto in automobili:
                if auto.snaga_motora >= snaga:
                    rezultat.append(auto)

        return rezultat

    def maximalna_brzina(self, brzina):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)

        rezultat = []

        if brzina > 0:
            for auto in automobili:
                if auto.max_brzina >= brzina:
                    rezultat.append(auto)

        return rezultat

    def pretraga_po_ceni(self, cena):
        automobili = self.ucitaj_automobile_iz_fajla(self.naziv_fajla)

        rezultat = []

        if cena > 0:
            for auto in automobili:
                if auto.cena >= cena:
                    rezultat.append(auto)

        return rezultat

    def __str__(self):
        rez = ""

        rez += "ID: " + str(self.__id) + "\n"
        rez += "Marka: " + self.__marka + "\n"
        rez += "Model: " + self.__model + "\n"
        rez += "Godiste: " + str(self.__godiste) + "\n"
        rez += "Snaga: " + str(self.__snaga_motora) + "\n"
        rez += "Brzina: " + str(self.__max_brzina) + "\n"
        rez += "Cena: " + str(self.__cena) + "\n"

        return rez


class KupovinaAutomobila:
    __auto: Automobil

    def __init__(self, auto):
        self.__auto = auto

    @property
    def auto(self):
        return self.__auto

    @auto.setter
    def auto(self, nova_vrednot):
        self.__auto = nova_vrednot
        
    def __str__(self):
        rez = "Kupovina automobila:\n"
        rez += str(self.__auto)
        return rez

class Korisnik:
    __ime: str
    __sifra: str
    __balans: int

    naziv_fajla = "korisnici.txt"

    def __init__(self, ime, sifra, balans=0):
        self.__ime = ime
        self.__sifra = sifra
        self.__balans = balans

    @property
    def ime(self):
        return self.__ime

    @property
    def sifra(self):
        return self.__sifra

    @property
    def balans(self):
        return self.__balans

    @ime.setter
    def ime(self, nova_vrednost):
        self.__ime = nova_vrednost
    
    @sifra.setter
    def sifra(self, nova_vrednost):
        self.__sifra = nova_vrednost
        
    @balans.setter
    def balans(self, value):
        self.__balans = value

    def ucitaj_korisnike_iz_fajla(self, naziv_fajla):
        korisnici = []

        try:
            with open(naziv_fajla, "r", encoding="utf-8") as fajl:
                for linija in fajl:
                    linija = linija.strip()

                    if linija == "":
                        continue

                    delovi = linija.split(":")

                    balans = int(delovi[2])

                    korisnik = Korisnik(delovi[0], delovi[1], balans)

                    korisnici.append(korisnik)

        except FileNotFoundError:
            print("Fajl ne postoji.")

        return korisnici

    def login(self, ime, sifra):
        korisnici = self.ucitaj_korisnike_iz_fajla(self.naziv_fajla)

        for korisnik in korisnici:
            if korisnik._Korisnik__ime == ime and korisnik._Korisnik__sifra == sifra:
                return korisnik

        return None

    def register(self, ime, sifra, balans=0):
        korisnici = self.ucitaj_korisnike_iz_fajla(self.naziv_fajla)

        for korisnik in korisnici:
            if korisnik._Korisnik__ime == ime:
                print("Korisnik već postoji.")
                return False

        fajl = open(self.naziv_fajla, "a", encoding="utf-8")

        linija = ime + ":" + sifra + ":" + str(balans) + "\n"

        fajl.write(linija)
        fajl.close()

        print("Uspešna registracija.")
        return True

    def azuriraj_balans_u_fajlu(self):
        korisnici = self.ucitaj_korisnike_iz_fajla(self.naziv_fajla)

        fajl = open(self.naziv_fajla, "w", encoding="utf-8")

        for korisnik in korisnici:
            if korisnik._Korisnik__ime == self.__ime:
                korisnik._Korisnik__balans = self.__balans

            linija = korisnik._Korisnik__ime + ":" + korisnik._Korisnik__sifra + ":" + str(korisnik._Korisnik__balans) + "\n"

            fajl.write(linija)

        fajl.close()
        
a1 = Automobil("Toyota", "Camry", 2020, 203, 220, 22000, 1)

def glavni_meni(korisnik):
    izbor = -1

    while izbor != 0:
        print("\n=== GLAVNI MENI ===")
        print("1) Automobili")
        print("2) Kupovina")
        print("3) Cena registracije")
        print("0) Izlaz")

        izbor = int(input("Izbor: "))

        if izbor == 1:
            opcija = -1

            while opcija != 0:
                print("\n--- AUTOMOBILI ---")
                print("1) Dodaj")
                print("2) Marka")
                print("3) Godiste")
                print("4) Snaga")
                print("5) Brzina")
                print("6) Cena")
                print("0) Nazad")

                opcija = int(input("Izbor: "))

                if opcija == 1:
                    marka = input("Marka: ")
                    model = input("Model: ")
                    godiste = int(input("Godiste: "))
                    snaga = int(input("Snaga: "))
                    brzina = int(input("Brzina: "))
                    cena = int(input("Cena: "))

                    automobili = a1.ucitaj_automobile_iz_fajla(a1.naziv_fajla)

                    max_id = 0

                    for auto in automobili:
                        if auto.id > max_id:
                            max_id = auto.id

                    novi = Automobil(marka, model, godiste, snaga, brzina, cena, max_id + 1)
                    novi.sacuvaj_automobil_u_fajl(novi.naziv_fajla)

                    print("Dodat auto.")

                elif opcija == 2:
                    marka = input("Marka: ")
                    rez = a1.pretraga_automobila_po_marki(marka)

                    for auto in rez:
                        print(auto)

                elif opcija == 3:
                    g = int(input("Godiste: "))
                    rez = a1.minimalno_godiste(g)

                    for auto in rez:
                        print(auto)

                elif opcija == 4:
                    s = int(input("Snaga: "))
                    rez = a1.minimalna_snaga_motora(s)

                    for auto in rez:
                        print(auto)

                elif opcija == 5:
                    b = int(input("Brzina: "))
                    rez = a1.maximalna_brzina(b)

                    for auto in rez:
                        print(auto)

                elif opcija == 6:
                    c = int(input("Cena: "))
                    rez = a1.pretraga_po_ceni(c)

                    for auto in rez:
                        print(auto)

        elif izbor == 2:
            
            
            budzet = korisnik.balans
            automobili = a1.ucitaj_automobile_iz_fajla(a1.naziv_fajla)

            dostupni = []

            for auto in automobili:
                if auto.cena <= budzet:
                    dostupni.append(auto)

            for auto in dostupni:
                print(auto)

            idk = int(input("ID kupovine: "))

            kupljen = None

            for auto in dostupni:
                if auto.id == idk:
                    kupljen = KupovinaAutomobila(auto)
                    break

            if kupljen:
                korisnik.balans = korisnik.balans - kupljen.auto.cena
                korisnik.azuriraj_balans_u_fajlu()

                a1.obrisi_automobil_iz_fajla(idk, a1.naziv_fajla)

                print(kupljen)
        elif izbor == 3:
            snaga = int(input("\nUnesite koliko konjskih snaga ima Vas auto: "))
            print(f"Cena je priblizno: {bib.racunanje_registracije(snaga)}")
            
while True:
    print("\n1) Login")
    print("2) Register")

    choose = int(input("Izbor: "))

    k1 = Korisnik("", "")

    if choose == 1:
        ime = input("Ime: ")
        sifra = input("Sifra: ")

        ulogovani = k1.login(ime, sifra)

        if ulogovani:
            print("Ulogovan.")
            print("Balans:", ulogovani.balans)

            glavni_meni(ulogovani)
            break

        else:
            print("Pogresni podaci.")

    elif choose == 2:
        ime = input("Ime: ")
        sifra = input("Sifra: ")
        balans = int(input("Balans: "))

        k1.register(ime, sifra, balans)


"""
def unos():
    a = int(input("Za koliko si sipao: "))
    b = int(input("Cena goriva: "))
    print(bib.prosecna_potrosnja(a, b))   
    pass
"""
