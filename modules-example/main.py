# Mit Import kann man in mehreren Dateien die Funktionen verwenden
# Erste Möglichkeit für Import
import taschenrechner as rechner

summe = rechner.addieren(2, 3)
differenz = rechner.subtrahieren(10, 7)
produkt = rechner.multiplizieren(4, 8)
quotient = rechner.dividieren(24, 8)
print(quotient)


# Zweite Möglichkeit für Import
# Hier werden automatisch alle Funktionen aus der Datei importiert
from taschenrechner import *

summe = addieren(2, 3)
differenz = subtrahieren(10, 7)
produkt = multiplizieren(4, 8)
quotient = dividieren(24, 8)
print(quotient)