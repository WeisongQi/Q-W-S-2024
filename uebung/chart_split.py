# Namensabfragen (Vor- und Nachname)

vorname = input ("Bitte geben Sie Ihren Vornamen ein: ")
#nachname = input ("Bitte geben Sie Ihren Nachnamen ein: ")


name =vorname.split(' ', maxsplit=2)
#print (f"Hallo, {name} .")

for part in name :
    print(part)
    