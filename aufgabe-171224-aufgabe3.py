# Aufgabe 3


# Definieren von Funktionen
def num_input():
    num = input()

    if num.isdigit():
        # print(float(num))
        return float(num)
    else:
        print("error")
        return num_input()


# Fläche eines Rechtecks
def calc_area():
    print("Enter a number for Width : ")
    w = num_input()
    print("Enter a number for length : ")
    l = num_input()
    print(f"Die Fläche dieses Vierecks beträgt: {w * l}")


# miles to KM
def miles_to_KM():
    print("Enter a number for miles : ")
    m = num_input()
    km = m * 1.60934
    # print(type(km))
    print(f"{m} miles = {km} Kilometers")


# KM to miles
def KM_to_miles():
    print("Enter a number for Kilometers : ")
    km = num_input()
    m = km / 1.60934
    # print(type(km))
    print(f"{m} miles = {km} Kilometers")


#  fahrenheit to celsius
def fahrenheit_to_celsius():
    print("Enter a number for fahrenheit : ")
    fahr = num_input()
    cels = (fahr - 32) * 5 / 9
    print(f"{cels} Grad Celsius = {fahr} Grad Fahrenheit")


# Taschenrechner


# Funktionen
def add(x, y):
    print(f"Zahl-A + Zahl-B ergibt {x+y}")


def subtract(x, y):
    print(f"Zahl-A - Zahl-B ist {x-y}")


def mult(x, y):
    print(f"Zahl-A * Zahl-B ist {x*y}")


def div(x, y):
    print(f"Zahl-A / Zahl-B ist {x/y}")


def taschenrechner():

    f_aufruf = input(
        "Welche Rechenmethode wählen Sie: 1:Addition, 2:Subtraktion, 3:Multiplikation, 4:Division (A,S,M;D): "
    )
    print("Enter a number : ")
    x = num_input()
    print("Enter a number : ")
    y = num_input()

    if f_aufruf in ["A", "a", "1"]:
        add(x, y)
    elif f_aufruf in ["S", "s", "2"]:
        subtract(x, y)
    elif f_aufruf in ["M", "m", "3"]:
        mult(x, y)
    elif f_aufruf in ["D", "d", "4"]:
        div(x, y)
    else:
        print("Sie haben einen Fehler eingegeben.")
        return taschenrechner()


# main
calc_area()
miles_to_KM()
KM_to_miles()
fahrenheit_to_celsius()
taschenrechner()
