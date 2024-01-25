liste = [1, 2, 3, "Mia", "Lea", "Anja"]

try:
    index = int(input("Gib bitte einen Index ein: "))
    print(liste[index])
except IndexError as ex:
    print(f"Der Zugriff ist fehlgeschlagen. \n{ex}")
except ValueError:
    print("Bitte gib eine Zahl ein")
# Fängt jeden auftretenden Fehler auf
# except Exception as ex:
    # print(f"Es ist ein Fehler aufgetreten. \n{ex}")
finally:
    print("Suche abgeschlossen!")



try:
    f = open("test.txt", "w")
    f.write("Hallo Welt")
except Exception:
    pass
finally: 
      f.close()