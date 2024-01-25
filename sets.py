# Elemente werden nicht der Reihenfolge nach angezeigt
# Sich widerholende Element werden nur einmal angezeigt
print({12, 22, True, 34, 49, 5, "Mia"})

# Prüfen, ob das Element schon vorgekommen ist
seen = set()


# Prüft ob Element im Set vorhanden ist, True oder False
zahlen = {0, 1, 2, 3, 4, 5, 7, 8}
print(5 in zahlen)


# Fügt ein Element zum Set hinzu
# Duplikat wird nicht hinzugefügt
zahlen = {0, 1, 2, 3, 4, 5, 7, 8}
zahlen.add(20)
print(zahlen)


# Element aus dem Set löschen
zahlen = {0, 1, 2, 3, 4, 5, 7, 8}
zahlen.remove(3)
print(zahlen)


# Löscht alle Elemente aus dem Set; copy() erstellt eine Kopie von dem Set
zahlen = {0, 1, 2, 3, 4, 5, 7, 8}

zahlen_kopie = zahlen.copy()
zahlen.clear()
print(zahlen_kopie)


# Set in Liste umwandeln und die Liste z.B. sortieren
setZahlen = {8, 4, 7, 3, 5, 6, 9}
liste = list(setZahlen)
print(type(list(liste)))

liste.sort()
print(liste)