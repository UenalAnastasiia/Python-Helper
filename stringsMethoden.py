# Alle Methoden für Stings anzeigen
print(dir(str))

#zfill - füllt den STring von links mit Nullen bis zur angegebenen Länge
print("Anastasiia".zfill(12))

#upper - schreibt alle Buchstaben groß
print("Anastasiia".upper())

#lower - schreibt alle Buchstaben klein
print("ANAStasiia".lower())

#capitalize - schreibt den ersten Buchstaben groß, alle anderen klein
print("ANAStasiia".capitalize())

#isupper - prüft, ob alle Buchstaben Großbuchstaben sind
print("Anastasiia".isupper())

#islower - prüft, ob alle Buchstaben Kleinbuchstaben sind
print("anastasiia".islower())

#isnumeric - prüft, ob alle Elemente Zahlen sind
print("Anastasiia1234".isnumeric())

#isalpha - prüft, ob alle Elemente Buchstaben sind
print("Anastasiia".isalpha())

#split - erstellt eine Liste mit Einträgen, die durch das eingegebene Zeichen getrennt wurden
print("Anastasiia;Pamela;Anna;Lea".split(";"))

#\n - Zeilenumbruch
print("Anastasiia\nPamela\nAnna\nLea")

#splitlines - erstellt eine Liste mit Einträgen, die durch den Zeilenbruch getrennt wurden
print("Anastasiia\nPamela\nAnna\nLea".splitlines())

#strip - entfernt die Leerzeichen vor und hinter dem Wort
print("   Anastasiia   ".strip())

#replace - ersetzt das erste angegebene Zeichen durch das zweite angegebene Zeichen
print("anastasiia".replace("a", "A"))

#count - zählt wie oft ein Zeichen vorkommt
print("anastasiia".count("a"))

#index - zeigt an welcher Stelle das Zeichen ist
print("anastasiia".index("t"))

#find - zeigt an welcher Stelle das Zeichen ist, aber ohne Fehler wenn das Zeichen nicht vorhanden ist, zeigt dann den Index -1
print("anastasiia".find("t"))

#in - zeigt, ob das Zeichen vorhanden ist
print("Stein" in "Wasserfall, Stein, Meer, Wüste")