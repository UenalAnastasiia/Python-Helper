#Tuple sind fixe Werte, die an bestimmten Positionen existieren und die Datenstruktur ist unveränderbar

# Leeres Tupel 
print(len(()))

# Tupel mit 3 Elementen
print(len((1, 2, 3)))


# Element aus Tupel anzeigen
test = (1, 2, 30, 45, 32, 67)
print(test[3])
print((1, 2, 30, 45, 32, 67)[3])


# Result wird den Typ tulpe haben
def addieren(a, b):
    summe = a + b
    return a, b, summe

result = addieren(1, 4)
print(type(result))


# Kombination aus mehreren Tupeln
ergebnis = (1, 2, 3) + (4, 5)
print(ergebnis)


# Zählen wie oft ein Element vorkommt
tupleList = (8, 4, 8, 7, 3, 5, 8, 6, 9)
result = tupleList.count(8)
print(result)


# Zeigt die Position des Elements in der Tupel
zahlen = (0, 1, 2, 3, 4, 5, 7, 8)
position = zahlen.index(7)
print(position)


# Tupel in Liste umwandeln und die Liste z.B. sortieren
tupleZahlen = (8, 4, 7, 3, 5, 6, 9)
liste = list(tupleZahlen)
print(type(list(liste)))

liste.sort()
print(liste)