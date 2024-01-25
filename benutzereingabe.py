# Input gibt immer ein String zurück
# Input ist eine blockierende Anweisung => das Programm lädt nicht weiter, bis man in Input etwas eingegeben hat

name = input("Gib deinen Name ein: ")
print(f"Hallo {name}!")


jahr = int(input("In welchem Jahr wurdest du geboren?\n"))
alter = 2024 - jahr
print(f"DU bist {alter} Jahre alt")