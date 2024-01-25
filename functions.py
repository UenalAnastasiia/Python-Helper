# Zeigt in der Konsole das Ergebnis
print("Hallo Welt")

# def leitet eine Funtion ein
# Python ist auf Einrückungen der Zeilen strukturiert => so weiß Python welcher Block zu welcher Funktion gehört (wie in JS die {})
# f wird gesetzt, wenn im String eine Variable vorkommt
def sag_hallo(name, surname):
    print(f"Hallo {name} {surname}")


sag_hallo("Anna", "Mueller")


# pass - No Operation => wird verwendet, wenn die Funktion nichts ausführen soll
def leere_func():
    pass


# return statement
def addieren(a, b):
    summe = a + b
    return summe * 10

returnResult = addieren(3, 4)
print(f"Summe: {returnResult}")


# args => wird als * markiert
# Wird als Tuple übergeben
# mit args kann man beliebig viele Werte übergeben oder keine
# Positional Arguments kommen als erstes in den Funktionsparametern, danach die optionalen args
def addieren(vorname, nachname, *summanden):
    s = sum(summanden)
    print(f"Ergebnis von {vorname} {nachname}: {s}")

addieren("Anna", "Mueller", 1, 2, 3, 4, 5)


# kwargs - keyword args => werden mit ** definiert
# Wird als Dictionary übergeben mit Keys und Values
# Wenn ein Key nicht übergeben wurde, wird das Ergebnis None sein
def teilnehemer(**daten):
    vn = daten.get("vorname")
    nn = daten.get("nachname")
    alt = daten.get("alter", "-")
    gs = daten.get("geschlecht", "N/A")
    print(f"{vn} {nn}; Alter: {alt}; Geschlecht: {gs}")

teilnehemer(nachname="Müller", vorname="Anna", alter=29)


# Aufrufreihenfolge in Funktionen:
    # 1. Positional Arguments
    # 2. *args
    # 3. **kwargs
def daten_erfassen(id, vorname, nachname, *geo, **daten):
    print(f"ID: {id}, Vorname: {vorname}, Nachname: {nachname}")
    print(f"GEO: {geo}")
    print(f"Contact: {daten}")

daten_erfassen(10, "Anna", "Müller", 2168, 34587, email="test@gmail.com", phonenumber="1236445", fax="45663")