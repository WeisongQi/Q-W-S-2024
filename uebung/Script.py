""" print ("Hallo Welt.")

First_Name = "Anna"
Last_Name = "Muster"

print (First_Name + " " + Last_Name) 

length = len(Last_Name)

print (length)

Last_Name =  input ("Bitte giben Sie Name:")

print (Last_Name)

zahl1 = 2
zahl2 = 10

print ("Zahl 1 + Zahl 2:", zahl1 + zahl2)
print ("Zahl 1 * Zahl 2:", zahl1 * zahl2)
print ("Zahl 2 / Zahl 1:", zahl2 / zahl1)

for num in range(1,6):
    print (num)

print (range(1,8))

print (First_Name + " " + Last_Name)     

char_list = list(Last_Name) 

print (char_list)

list_date = [1, 2, 3]
tuple_date = tuple(list_date)

print (tuple_date) """

# 初始化计数器变量
call_count = 0


def my_function():
    global call_count
    call_count += 1
    print(f"函数被调用的次数: {call_count}")


# 调用函数
my_function()  # 输出：函数被调用的次数: 1
my_function()  # 输出：函数被调用的次数: 2
my_function()  # 输出：函数被调用的次数: 3
