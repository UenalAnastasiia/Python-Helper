numberList = [0, 2, 4, 6, 8, 10]
print(numberList[4])
print(numberList[2:4])


# Liste zur Liste hinzufügen
zahlen = [0, 1, 2, 3, 4, 5]
weitere_zahlen = [10, 11, 12, 13, 14, 15]

ergebnis = zahlen + [10, 11, 12, 13, 14, 15]
print(ergebnis)


# [0, 1, 0, 1, 0, 1]
bits = [0, 1]
print(bits * 3)


# Element zur Liste hinzufügen
zahl = [0, 1]
zahl.append(2)
print(zahl)


# Liste aufsteigend sortieren
zahlen_sort = [8, 4, 7, 3, 5, 6, 9]
zahlen_sort.sort()
print(zahlen_sort)


# Liste absteigend sortieren
zahlen_sort = [8, 4, 7, 3, 5, 6, 9]
zahlen_sort.sort(reverse=True)
print(zahlen_sort)


# Zählen wie oft ein Element vorkommt
zahlen_sort = [8, 4, 8, True, 7, 3, 5, "Mia", 8, 6, 9]
result = zahlen_sort.count(8)
print(result)


# Element aus der Liste löschen
zahlen_sort = [8, 4, 8, True, 7, 3, 5, "Mia", 8, 6, 9]
zahlen_sort.remove(True)
zahlen_sort.remove("Mia")
print(zahlen_sort)


# Zu einer bestimmten Index-Position wird ein neuer Wert hinzugefügt
zahlen = [0, 1, 2, 3, 4, 5, 7, 8]
zahlen.insert(6, 10)
print(zahlen)


# Löscht alle Elemente aus der Liste; copy() erstellt eine Kopie von der Liste
zahlen = [0, 1, 2, 3, 4, 5, 7, 8]

zahlen_kopie = zahlen.copy()
zahlen.clear()
print(zahlen_kopie)


# Zeigt die Position des Elements in der Liste
zahlen = [0, 1, 2, 3, 4, 5, 7, 8]
position = zahlen.index(7)
print(position)


# Prüft ob Element in der Liste vorhanden ist, True oder False
zahlen = [0, 1, 2, 3, 4, 5, 7, 8]
check = 6 in zahlen
print(check)

# Führt die Strings in der Liste mit dem angegebenem Zeichen zusammen
buchstaben = ["A", "N", "N", "A"]
print("".join(buchstaben))