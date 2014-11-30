# -*- coding: cp1250 -*-

menu={}
moje_menu={}

with open("menu_restauracji.txt") as moje_menu:
    moje_menu = moje_menu.readlines()
    
for linia in moje_menu:
    danie = linia.split(":")[0]
    cena = float(linia.split(":")[1])
    menu[danie] = cena

def zamowienie(zamowienie):
    cena = 0
    for i in zamowienie:
        if i in menu:
            cena+=menu[i]
    return "Koszt zam�wienia wynosi " + str(cena*1.10) + " z�."

print zamowienie(["kurczak z pesto", "szarlotka", "sa�atka z kozim serem"])