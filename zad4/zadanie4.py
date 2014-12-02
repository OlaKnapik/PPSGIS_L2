# -*- coding: cp1250 -*-

class Buty(object):
    
    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = model
    def get_cena(self):
        return self.cena
    def set_cena(self, cena):
        self.cena = cena
    def get_rozmiar(self):
        return self.rozmiar
    def set_rozmiar(self, rozmiar):
        self.rozmiar = rozmiar

    def __init__(self, model, cena, rozmiar, material):
        self.model = model
        self.cena = cena
        self.rozmiar = rozmiar
        self.material = material    
        
    def kup(self, Osoba):
        if Osoba.get_portfel() > self.cena :
            Osoba.set_portfel(Osoba.get_portfel() - self.cena)
            print "Buty o modelu "+ self.get_model()  +" zostały kupione za " + str(self.get_cena()) + " zł."
            print "W portwelu uzytkownika " + Osoba.get_imie() + " pozostało " + str(Osoba.get_portfel()) + " zł."
        else:
            print Osoba.get_imie() + "! Masz za mało pieniędzy."
        
    def wyczysc(self):
        print "Buty są teraz czyste!"
        
    def zaloz(self, Osoba):
        if Osoba.get_roz()> self.rozmiar:
            print str(Osoba.get_imie()) + "! To nie Twój rozmiar!"
        else:
            print str(Osoba.get_imie()) + " ma założone buty, model: " + self.get_model() + " ."
        

class Osoba(object):
    def get_roz(self):
        return self.roz
    def set_roz(self, roz):
        self.roz = roz
    def get_imie(self):
        return self.imie
    def set_imie(self, imie):
        self.imie = imie
    def get_portfel(self):
        return self.portfel
    def set_portfel(self, portfel):
        self.portfel = portfel

    def __init__(self, imie, roz, portfel):
        self.imie = imie
        self.roz = roz
        self.portfel = portfel


class Buty_zimowe(Buty):
    
    def __init__(self, model, cena, rozmiar, material, czy_cieple):
        Buty.__init__(self, model, cena, rozmiar, material)
        self.czy_cieple = czy_cieple
        
    def get_czy_cieple(self):
        return self.czy_cieple
    def set_czy_cieple(self, czy_cieple):
        self.czy_cieple = czy_cieple

        
    def idz_po_sniegu(self):
        if self.czy_cieple == True:
            print "Ale miło spacerować zimą :)"
        else:
            print "W tych butach będzie Ci za zimno! Zmień je."
            
class Akcesoria_plywackie(object):
    
    def __init__(self, czy_przemaka):
        self.czy_przemaka = czy_przemaka
        
    def get_czy_przemaka(self):
        return self.czy_przemaka
    def set_czy_przemaka(self, czy_przemaka):
        self.czy_przemaka = czy_przemaka

class Buty_do_plywania(Buty, Akcesoria_plywackie):
    
    def __init__(self, model, cena, rozmiar, material, czy_przemaka):
        Buty.__init__(self, model, cena, rozmiar, material)
        Akcesoria_plywackie.__init__(self, czy_przemaka)
    
    def plyn(self):
        if self.czy_przemaka == True:
            print "Nie da sie pływać."
        else:
            print "No to płyniemy!"


Heniek = Osoba("Heniek", 40, 290)
Kasia = Osoba("Kasia", 38, 550)

kozaki1 = Buty_zimowe("Ładny1", 230, 40, "zamsz", False)
kozaki2 = Buty_zimowe("Ładny2", 280, 40, "ekoskóra", True)

pantofel = Buty("Exclusive", 320, 36, "skóra")
plywaki = Buty_do_plywania("Delfin", 100, 38, "plastik", True)
plywaki2 = Buty_do_plywania("ProDelfin", 100, 38, "guma", False)


# przykłady użycia :

pantofel.kup(Heniek)
print
pantofel.kup(Kasia)
print
pantofel.zaloz(Kasia)
print
kozaki2.kup(Kasia)
kozaki2.kup(Heniek)
kozaki2.wyczysc()
print
kozaki1.zaloz(Heniek)
kozaki1.idz_po_sniegu()
kozaki2.zaloz(Heniek)
kozaki2.idz_po_sniegu()
print
plywaki.zaloz(Kasia)
plywaki.plyn()
plywaki2.zaloz(Kasia)
plywaki2.plyn()
