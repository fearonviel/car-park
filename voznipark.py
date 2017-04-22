#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from operator import attrgetter

#CLASS VOZILO
class Vozilo():
    def __init__(self, znamka, model, prevozeni_km, datum_servisa):
        self.znamka = znamka
        self.model = model
        self.prevozeni_km = prevozeni_km
        self.datum_servisa = datum_servisa

    def izpisi_znamko(self):
        print(self.znamka + " " + self.model)


#FUNKCIJE

def izpisi_vozila(seznam_vozil):
    for index, vozilo in enumerate(seznam_vozil):
        print str(index + 1) + "   " + vozilo.znamka + " " + vozilo.model
    if not seznam_vozil:
        print("Na seznamu ni vozil.")
    print ""


def izpisi_vozila_podrobno(seznam_vozil):
    for index, vozilo in enumerate(seznam_vozil):
        print(str(index + 1) + "   " + vozilo.znamka + " " + vozilo.model + ", " + vozilo.prevozeni_km + " km, Datum zadnjega servisa: " + vozilo.datum_servisa)
    if not seznam_vozil:
        print("Na seznamu ni vozil.")
    print ""


def izpisi_podrobno(seznam_vozil):
    if not seznam_vozil:
        print("Na seznamu ni vozil.")
    else:
        print("Za katero vozilo želite podrobnejše podatke? ")
        for index, vozilo in enumerate(seznam_vozil):
            print str(index + 1) + "   " + vozilo.znamka + " " + vozilo.model
        print ""

        izbor_vozila = raw_input("> ")
        izbrano_vozilo = seznam_vozil[int(izbor_vozila) - 1]

        izbrano_vozilo.izpisi_znamko()
        print("Število prevoženih km: " + izbrano_vozilo.prevozeni_km)
        print("Datum zadnjega servisa: " + izbrano_vozilo.datum_servisa)
        print ""


def dodaj_novo_vozilo(seznam_vozil):
    vnos_znamke = raw_input("Vnesite znamko: ")
    vnos_modela = raw_input("Vnesite model: ")
    vnos_km = raw_input("Vnesite število prevoženih kilometrov: ")
    vnos_servisa = raw_input("Vnesite datum zadnjega servisa: ")
    novo_vozilo = Vozilo(vnos_znamke, vnos_modela, vnos_km, vnos_servisa)
    seznam_vozil.append(novo_vozilo)
    print ""
    seznam_vozil.sort(key=attrgetter("znamka"))


def izbrisi_vozilo(seznam_vozil):
    print("Katero vozilo želite izbrisati? ")
    """for index, vozilo in enumerate(seznam_vozil, start=1):"""
    for index, vozilo in enumerate(seznam_vozil):
        print str(index + 1) + "   " + vozilo.znamka + " " + vozilo.model
    print ""

    izbor_vozila = raw_input("> ")
    izbrano_vozilo = seznam_vozil[int(izbor_vozila) - 1]

    seznam_vozil.remove(izbrano_vozilo)
    print "Vozilo je bilo uspešno izbrisano!"
    print ""


def uredi_vozilo(seznam_vozil):
    print("Katero vozilo želite urediti? ")
    for index, vozilo in enumerate(seznam_vozil):
        print str(index + 1) + "   " + vozilo.znamka + " " + vozilo.model
    print ""

    izbor_vozila = raw_input("> ")
    izbrano_vozilo = seznam_vozil[int(izbor_vozila) - 1]
    print("Katero polje bi radi posodobili? \n1. Število prevoženih kilometrov \n2. Datum zadnjega servisa?")
    vnos_novih_podatkov = raw_input("> ")
    if vnos_novih_podatkov == "1":
        print("Trenutno stanje kilometrov je: " + izbrano_vozilo.prevozeni_km)
        novi_km = raw_input("Vnesite novo število kilometrov: ")
        izbrano_vozilo.prevozeni_km = novi_km
        print("Število kilometrov je posodobljeno.")
        print ""
    elif vnos_novih_podatkov == "2":
        print("Zadnji vnešeni datum servisa je: " + izbrano_vozilo.datum_servisa)
        nov_datum = raw_input("Vnesite nov datum zadnjega servisa: ")
        izbrano_vozilo.datum_servisa = nov_datum
        print("Datum zadnjega servisa je posodobljen.")
        print""
    else:
        print("Prosimo vnesite število od 1 do 2.")

#SEZNAM VOZIL

vozilo1 = Vozilo("Honda", "Civic", "31.000", "2.3.2017")
vozilo2 = Vozilo("Suzuki", "Swift", "189.000", "27.6.2016")
vozilo3 = Vozilo("Peugeot", "508", "98.000", "11.10.2016")
vozilo4 = Vozilo("Renault", "Clio", "123.000", "17.8.2016")
vozilo5 = Vozilo("Audi", "A3", "46.000", "1.1.2016")
seznam_vozil = [vozilo1, vozilo2, vozilo3, vozilo4, vozilo5]
seznam_vozil.sort(key=attrgetter("znamka"))

#PROGRAM

print("Pozdravljeni.")
while True:
    print("Izberite opcijo: \n1. Vnos vozila \n2. Izpis vseh vozil \n3. Podrobnejši izpis vseh vozil \n4. Podrobnejši izpis vozila \n5. Izbris vozila \n6. Urejanje vozila \n7. Zaključi")
    user_input = raw_input("> ")
    if user_input == "1":
        dodaj_novo_vozilo(seznam_vozil)

    elif user_input == "2":
        izpisi_vozila(seznam_vozil)

    elif user_input =="3":
        izpisi_vozila_podrobno(seznam_vozil)

    elif user_input == "4":
        izpisi_podrobno(seznam_vozil)

    elif user_input == "5":
        izbrisi_vozilo(seznam_vozil)

    elif user_input == "6":
        uredi_vozilo(seznam_vozil)

    elif user_input == "7":
        shrani_spremembe = raw_input("Želite shraniti spremembe v datoteko vozni_park.txt? Da/ne? ").lower()
        if shrani_spremembe == "da":
            with open("vozni_park.txt", "w+") as vozni_park_file:
                vozni_park_file.write("Stanje vozil na: " + time.strftime("%d/%m/%Y\n---------------------------\n"))
                for index, vozilo in enumerate(seznam_vozil):
                    vozni_park_file.write(str(index) + "   " + vozilo.znamka + " " + vozilo.model + ", " + vozilo.prevozeni_km + " km, Datum zadnjega servisa: " + vozilo.datum_servisa+"\n")
            print("Spremembe uspešno shranjene. Na svidenje.")
            break
        else:
            print("Na svidenje.")
            break

    else:
        print("Prosim vnesite številko od 1 do 7.")


