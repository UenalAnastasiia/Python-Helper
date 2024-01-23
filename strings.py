name = "Anastasiia"

#zeigt die Länge des Strings
print(len(name))

#3 ist der Index, wird das vierte Element angezeigt
print("Anastasiia"[3])

#Elemente werden vom letzten gezählt => letztes Eleemnt im String ist -1
print("Anastasiia"[-6])

#zeigt letztes Element
n = len("Anastasiia")
print("Anastasiia"[n-1])
print("Anastasiia"[-1])

#Wird die angegebe Zeichenkette angezeigt => hier Ana
name = "Anastasiia"
print(name[0:3])
print(name[:3])
#zeigt nach dem Index alle Elemente an => hier stasiia
print("Anastasiia"[3:])


#Strings konkatenieren
a = "Hallo"
b = " "
c = "Python"
d = "!"
print(a + b + c + d)
print(d*3)