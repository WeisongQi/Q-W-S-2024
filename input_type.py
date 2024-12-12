person1 = input("Gib das Alter von Person1 ein:  ")
person2 = input("Gib das Alter von Person2 ein:  ")

print (f"Wir geben nun das von Ihnen eingegebene Datenformat aus. {type(person1)} {person1}  \n {type(person2)} {person2} ")
print (f"Machen wir zwei Alter zusammen legen: {person1 + person2} oder {int(person1) + int(person2)}")


""" print (type(person1),person1)
print (type(person2),person2)

person1_int = int (person1)
person2_int = int (person2)

add_type1 = person1 + person2
add_type2 = person1_int + person2_int

print (add_type1)
print (add_type2) """