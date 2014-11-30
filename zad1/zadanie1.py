# -*- coding: cp1250 -*-

with open("dowolnytekst.txt", "r") as tekst:
    a = (tekst.read()).lower()

wszystkie = a.translate(None,'.,?![]{}();:-_\n').split()

wynik = {}
for i in wszystkie:
    if i in wynik:
        wynik[i] = wynik[i] + 1
    else:
        wynik[i] = 1

wynik_lista = [(s,i) for i,s in wynik.items()]
wynik_lista.sort(reverse = True)

for element in wynik_lista:
    statystyka = "%s: %d" % (element[1], element[0]) + '\n'
    print statystyka

with open("statystyki.txt", "w") as statystyki:
    statystyki.writelines("Słowo: ilość w tekście" + "\n")
    statystyki.writelines("(od najczęściej występujących) " + "\n")
    statystyki.writelines("\n")
    for element in wynik_lista:
        statystyki.writelines("%s: %d" % (element[1], element[0]) + "\n")
