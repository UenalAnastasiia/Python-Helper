telefonbuch = {
    "Anna" : "49212456789",
    "Mia": "55564934654",
    3: "563287462"
}

# Bei get-Methode wird kein Fehler angezeigt, wenn der Key nicht vorhanden ist
# get-Methode ist besser, als mit eckingen Klammern aufzurufen
print(telefonbuch.get("Anna"))
print(telefonbuch["Anna"])
print(len(telefonbuch))


passwort_hashes = {
    "abc343" : "vfre564v64bsf64b",
    "3456" : "vfre564v64bsf64b",
    "3325" : "vfre564v64bsf64b",
    "4444" : "55555"
}

# Ergebnis None, wenn der Key nicht vohanden ist
print(passwort_hashes.get("geheimespw"))


# Ergebnis 111111, wenn der Key nicht vohanden ist
print(passwort_hashes.get("geheimespw", "111111"))


# Wert vom Key verändern oder einen neuen Key und Wert hinzufügen
passwort_hashes["4444"] = "77777"
print(passwort_hashes["4444"])


# Wert vom Key updaten 
passwort_hashes.update({"4444" : "8888"})

# Einen Eintrag löschen
del passwort_hashes["4444"]
print(passwort_hashes)


# Eine Kopie erstellen und alle Daten aus dem dictionary löschen
kopie = passwort_hashes.copy()
passwort_hashes.clear()


# Alle Keys werden in einer Liste angezeigt
print(list(passwort_hashes.keys()))


# Alle Values werden in einer Liste angezeigt
print(list(passwort_hashes.values()))