## Aufgabe 1: Einfache Entscheidungen mit `if`-Statements (25 Punkte)

**Ziel:** Verstehen, wie Entscheidungen im Code in Arbeitsschritte übersetzt werden können.

Code-Beispiel:

```python
    zahl = int(input("Gib eine Zahl ein: "))
    if zahl > 10:
        print("Die Zahl ist größer als 10.")
    else:
        print("Die Zahl ist 10 oder kleiner.")
```

- Schreibe die Arbeitsschritte auf.

---
-   Zeile 8 : Der Benutzer muss eine Zahl **str** eingeben, die in ``int`` umgewandelt und der Variablen `zahl` zugewiesen wird. 
-   Zeile 9 + 10 : Es wird überprüft, ob die Zahl größer als 10 ist. Wenn dies der Fall ist, wird der Text (Zeile 10) "Die Zahl ist größer als 10." ausgegeben.
-   Zeile 11 + 12: Wenn die Zahl kleiner oder gleich 10 ist, wird der Text (Zeile 12)"Die Zahl ist 10 oder kleiner." ausgegeben.

## Aufgabe 2: Listen verstehen und mit Python erstellen (20 Punkte)

**Ziel:** Verstehen, wie Datenstrukturen wie Listen verwendet werden können.

Code-Beispiel:

```python
    zahlen = [1, 2, 3, 4, 5]
    print("Die erste Zahl ist:", zahlen[0])
    print("Die letzte Zahl ist:", zahlen[-1])
```

- Schreibe die Arbeitsschritte auf.

---
-   Zeile 29 : Eine Liste wird mit den Zahlen 1,2,3,4 und 5 definiert. Diese Liste wird der Variablen `zahlen` zugewiesen. Diese Liste besteht aus ganzen Zahlen **int**.
-   Zeile 30 : Der Wert an der Position 0 in der Liste `zahlen`wird ausgegeben.
-   Zeile 31 : Der Wert an der letzten Position in der Liste `zahlen` wird ausgegeben.


**Zusatzaufgabe:** Erstelle selbst eine Liste mit Wochentagen und schreibe die Arbeitsschritte auf.

---

- Liste mit Wochentagen erstellen
```python
    wochentage = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag" ]
    print("Der erste Wochentag ist:", wochentage[0])
    print("Der letzte Wochentag ist:", wochentage[-1])
```
---
--- Zeile 48 : Liste mit den Wochentagen erstellen und der Variablen `wochentage` zuweisen. Diese Liste besteht aus Zeichenketten **str**.
--- Zeile 49 : Der Wert an der Position 0 in der Liste `wochentage` wird ausgegeben.
--- Zeile 50 : Der Wert an der letzten Position in der Liste `wochentage` wird ausgegeben.


## Aufgabe 3: Entscheidungslogik erweitern (25 Punkte)

**Ziel:** Die Funktionsweise von mehreren Bedingungen in Python verstehen und in Arbeitsschritte übertragen.

Code-Beispiel:

```python
    zahl = int(input("Gib eine Zahl ein: "))
    if zahl > 0:
        print("Die Zahl ist positiv.")
    elif zahl < 0:
        print("Die Zahl ist negativ.")
    else:
        print("Die Zahl ist null.")
```

- Schreibe die Arbeitsschritte auf.

---
-  Zeile 64 : Der Benutzer muss eine Zahl **str** eingeben, die in ``int`` umgewandelt und der Variablen `zahl` zugewiesen wird. 
-  Zeile 65 : Es wird überprüft, ob die Zahl größer als 0 ist. Wenn dies der Fall ist, wird der Text (Zeile 66) "Die Zahl ist positiv." ausgegeben.
-  Zeile 67 : Es wird überprüft, ob die Zahl kleiner als 0 ist. Wenn dies der Fall ist, wird der Text (Zeile 68) "Die Zahl ist negativ." ausgegeben.
-  Zeile 69 : Wenn die Zahl 0 ist, wird der Text (Zeile 70) "Die Zahl ist null." ausgegeben.

## Aufgabe 4: Funktionen verstehen (20 Punkte)

**Ziel:** Lernen, wie Funktionen in Python definiert werden und was in jedem Arbeitsschritt passiert.

Code-Beispiel:

```python
    def ist_gerade(zahl):
        if zahl % 2 == 0:
            return True
        else:
            return False

    zahl = int(input("Gib eine Zahl ein: "))
    if ist_gerade(zahl):
        print("Die Zahl ist gerade.")
    else:
        print("Die Zahl ist ungerade.")
```

- Schreibe die Arbeitsschritte auf.

---

-   Zeile 89 : Eine Funktion `ist_gerade` wird definiert, die eine Zahl als Parameter annimmt. Wenn die Zahl durch 2 geteilt ohne Rest ist, wird `True` zurückgegeben, andernfalls `False`. Die Funktion gibt einen booleschen Wert **bool** zurück.
-   Zeile 95 : Der Benutzer muss eine Zahl **str** eingeben, die in `int` umgewandelt und der Variablen `zahl` zugewiesen wird.
-   Zeile 96 : Es wird geprüft, ob die Funktion `ist_gerade` mit der Zahl als Argument `True` zurückgibt. Wenn ja, wird "Die Zahl ist gerade." ausgegeben, andernfalls "Die Zahl ist ungerade.".


## Aufgabe 5: Benutzerinteraktion (10 Punkte)

**Ziel:** Die Struktur eines Programms mit Benutzereingaben und Ausgaben analysieren.

Code-Beispiel:

```python
    name = input("Wie heißt du? ")
    alter = int(input("Wie alt bist du? "))
    print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")
```

- Schreibe die Arbeitsschritte auf.

---
-   Zeile 117 : Der Benutzer wird aufgefordert, seinen Namen einzugeben, der in der Variablen `name` gespeichert wird. `name ` ist ein **str**.
-   Zeile 118 : Der Benutzer wird aufgefordert, sein Alter **str** einzugeben, das in `int` umgewandelt und der Variablen `alter` zugewiesen wird.
-   Zeile 119 : Der Name und das Alter des Benutzers werden in einem Satz ausgegeben, wobei das Alter in 10 Jahren berechnet wird.

