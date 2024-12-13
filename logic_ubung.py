# Aufgabe 1
a_input = input("Bitte geben Sie ein Zahl ein: ")
b_input = input("Bitte geben Sie ein Zahl ein: ")

a = int(a_input)
b = int(b_input)

if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
elif a == b:
    print(f"{a} = {b}")
elif a != b:
    print(f"{a} != {b}")

if a > b or a == b:
    print(f"{a} >= {b}")
if a < b or a == b:
    print(f"{a} <= {b}")

""" if a < b:
    print("a is less than b.")
elif a <= b:
    print("a is less than or equal to b.")
elif a > b:
    print("a is greater than b.")
elif a >= b:
    print("a is greater than or equal to b.")
elif a == b:
    print("a is equal to b.")
elif a != b:
    print("a is not equal to b.") """
