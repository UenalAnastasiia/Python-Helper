# If Else Anweisungen

passwort = input("Gib dein Passwort ein: ")

if passwort == "abc123":
    print("Richtiges Passwort")
else:
  print("Falsches Passwort")


note = input("Gib deine Note ein: ")

if note == "1":
    print("Sehr gut")
elif note == "2":
    print("Gut")
elif note == "3":
    print("Befried.")
elif note == "4":
    print("Ausreich.")
elif note == "5":
    print("Mangelh.")
else:
    print("Ungenügend")


note = int(input("Gib deine Note ein: "))

match note:
    case 1:
        print("Sehr gut")
    case 2:
        print("Gut")
    case 3:
        print("Befried.")
    case 4:
        print("Ausreich.")
    case 5:
        print("Mangelh.")
    case 6:
        print("Ungenügend")


noteList = [1,2]
match note:
    case [1]:
        print("Sehr gut")
    case [1,2]:
        print("Gut")


# For-Schleife - wird verwendet, wenn ein vorgegebener Bereich durchlaufen werden soll
# Kann nicht endlos laufen
        
passwörter = ["12345", "gehe1m", "test", "fkfpe"]

for passwort in passwörter:
    print(passwort)
    if len(passwort) < 5:
        break


# While-Schleife - wird verwendet, wenn kein vorgegebener Bereich durchlaufen werden soll, sondern der Abbruch von einer Bedingung abhängt
# Kann endlos laufen
    
x = 25
runde = 1

while x > 0:
    print(f"Runde {runde}")
    runde += 1
    x -= 1


namensListe = []
name = input("Gib deinen Name ein! (X) zum Abbruch: ")

while name != "X":
    namensListe.append(name)
    print(namensListe)
    name = input("Gib deinen Name ein! (X) zum Abbruch: ")


teilnehmerListe = []

while (teilnehmer := input("Gib einem Teilnehmer ein! (X) zum Abbruch: ")) != "X":
    teilnehmerListe.append(teilnehmer)

print(teilnehmerListe)