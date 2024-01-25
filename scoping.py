#Global scope => gilt nur für eine spezifische Datei, in der es definiert wurde
level = 0

def level_up():
    # Local scope
    local_level = 5
    print(f"Dein localer Level ist {local_level}")
    global level
    level += 1
    

level_up()
print(f"Dein globaler Level ist {level}")