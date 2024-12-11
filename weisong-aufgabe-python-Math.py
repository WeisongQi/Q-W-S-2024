"""  Aufgabe 3.1  """
print ("--------------Aufgabe 3.1---------------")


zahle_a = input ("Bitte giben Sie ein Zahle a: ")
zahle_b = input ("Bitte giben Sie ein Zahle b: ")

add = (int(zahle_a) + int(zahle_b))
sub = (int(zahle_a) - int(zahle_b))
mul = (int(zahle_a) * int(zahle_b))
div = (int(zahle_a) / int(zahle_b))

print  ("a ist", zahle_a, "; b ist", zahle_b,".")

print  ("a + b =", add)
print  ("a - b =", sub)
print  ("a * b =", mul)
print  ("a / b =", div) 


""" Aufgabe 3.2 """
print ("--------------Aufgabe 3.2---------------")

note1 = 54
note2 = 68
note3 = 77

durch = ((note1 + note2 + note3) / 3)

print (" Die Noten sind :", note1,note2,note3)
print (" Der Durchschitt ist :", durch)


""" Aufgabe 3.3 """
print ("--------------Aufgabe 3.3---------------")

km = input ("Bitte giben Sie die Kilometer-Zahle : ")
m = 0.621371
meil = (int(km) / m)
print ("Das Kilometer umtechnet in Meilen! Gleich Da!")

print (km,"Kilometer ist", int(meil), "Meilen")

print ("------------------END-------------------")