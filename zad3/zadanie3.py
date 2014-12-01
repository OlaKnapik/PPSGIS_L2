# -*- coding: cp1250 -*-

class liczba_zespolona:
    
    def get_rzeczywista(self):
        return self.__rzeczywsita
    def set_rzeczywista(self):
        return self.__rzeczywsita
   
    def get_urojona(self):
        return self.__urojona
    def set_urojona(self):
        return self.__urojona
   
    def __init__(self, rzeczywista, urojona):
        self.rzeczywista=rzeczywista
        self.urojona=urojona
    
    def dodaj(self, liczba_zespolona):
        suma=(self.rzeczywista+liczba_zespolona.rzeczywista,self.urojona+liczba_zespolona.urojona )
        return suma
    
    def odejmij(self, liczba_zespolona):
        roznica=(self.rzeczywista-liczba_zespolona.rzeczywista,self.urojona-liczba_zespolona.urojona )
        return roznica
    
    def modul(self):
        modul=(self.rzeczywista**2+self.urojona**2)**(0.5)
        return modul
   
    def __str__(self):
        return str(self.rzeczywista)+" + "+str(self.urojona)+"i"
    pass

l1=liczba_zespolona(5,4)
l2=liczba_zespolona(4,3)

print "Pierwsza liczba zespolona to: "+str(l1) +", druga to: " +str(l2)+"."
print "Wynik dodawania: " + str(l1.dodaj(l2))+"."
print "Wynik odejmowania: " + str(l1.odejmij(l2))+"."
print "Moduł pierwszej liczby to: " + str(l1.modul()) + "."
print "Moduł drugiej liczby to: " + str(l2.modul()) + "."                             


