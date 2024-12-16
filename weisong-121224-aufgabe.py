# Aufgabe 1 Namensabfragen (Vor- und Nachname)

vorname = input("Bitte geben Sie Ihren Vornamen ein: ")
nachname = input("Bitte geben Sie Ihren Nachnamen ein: ")

print(f"Hallo, {vorname} {nachname}.")

# Aufgabe 2 Addition von Zahlen

zahle1 = input("Bitte geben Sie eine Zahl ein: ")
zahle2 = input("Bitte geben Sie noch eine Zahl ein:")

print(f"Die Zwei Zahlen summen ist: {int(zahle1) + int(zahle2)}.")

# Aufgabe 3 Einfache If-Bedingung
zahl = input("Bitte geben Sie eine Zahl ein: ")
zahl_int = int(zahl)

if zahl_int < 0:
    print("Die Zahl ist negativ.")
elif zahl_int == 0:
    print("Die Zahl ist Null.")
else:
    print("Die Zahl ist positiv.")
