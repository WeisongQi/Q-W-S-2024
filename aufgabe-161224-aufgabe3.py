# Taschenrechner


# Funktionen
def add(x, y):
    print(f"Zahl-A plus Zahl-B ergibt {x+y}")


def subtract(x, y):
    print(f"Zahl-A minus Zahl-B ist {x-y}")


def mult(x, y):
    print(f"Zahl-A multipliziert mit Zahl-B ist {x*y}")


def div(x, y):
    print(f"Zahl-A dividiert durch Zahl-B ist {x/y}")


# Funktion aufrufen

f_aufruf = input(
    "Welche Rechenmethode wählen Sie: Addition, Subtraktion, Multiplikation oder Division (A,S,M;D): "
)
f_aufruf_up = f_aufruf.upper()

# x_int = input("Bitte geben Sie Zahl-A ein: ")
# y_int = input("Bitte geben Sie Zahl-B ein: ")
x = int(input("Bitte geben Sie Zahl-A ein: "))
y = int(input("Bitte geben Sie Zahl-B ein: "))

if f_aufruf_up == "A":
    add(x, y)
elif f_aufruf_up == "S":
    subtract(x, y)
elif f_aufruf_up == "M":
    mult(x, y)
elif f_aufruf_up == "D":
    div(x, y)
else:
    print("Sie haben einen Fehler eingegeben.")
