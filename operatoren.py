# Rangfolge der Operatoren
# 1. Arithmetischen Operatoren (**, *, /, //, %, +, -)
# 2. Vergleichsoperatoren (^, <, <=, ==, !=, >=, >)
# 3. Logische Operatoren (not, and, or)


# Ergebnis 2.0, Ergebnis wird als Float angezeigt
print(30 / 15)

# Ergebnis 2; Hier wird nur der "vor Komma" Teil berücksichtigt
print(30 // 15)

# Modulo = 0
print(30 % 10)

# Modulo = 6
print(30 % 8)

# Ergebnis = 8
print(2**3)

# Ergebnis True
print(2 < 3 or 3 != 5)

# Ergebnis False
print(2 > 3 and 3 != 5)

# ^ - XOR-Operator; Ergebnis False
print(2 < 3 ^ 3 != 5)

# Ergebnis False
print(not True)