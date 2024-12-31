# date_1 = "2024.12.11"
# date_2 = "2024.12.12"

# print(f"date_1 > date_2 {date_1 > date_2}")


# def fage():
#    fage_inp = input("age")

#   print(fage_inp)


# fage()


# Name
""" def fname():
    fname_inp = input("name")

    # print(fname_inp)
    return f"name{fname_inp}"


fname()
fname()

numbers = [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "cherry"]

mix_list = [10, numbers, "orange", fruits]

mix_list.append("blueberry")

mix_list.insert(1, "annas")


print(mix_list)

sub_list = mix_list[0:4]
print(f"{sub_list} und {mix_list}")

length = len(mix_list)
print(length) """


# def add(a, b):
#     return a + b


# sum = add(3, 5)
# print(f"{add(4, add(3,5))}")

# import datetime

# # Creating a date object
# date_object = datetime.date(2024, 7, 17)
# print(f"{type(date_object)}", date_object)
# # Getting the day name
# day_name = date_object.strftime("%A")

# # Printing the day name
# print(f"The day name for {date_object} is: {day_name}")


# import calendar

# from datetime import datetime


# def wochentag_berechnen():
#     wochentag = input("Bitte nenne ein Datum ")
#     day = datetime.datetime.strptime(wochentag, "%d.%m.%Y").date()
#     print(f"Der {wochentag} ist ein {calendar.day_name[day.weekday()]}\n")


# def tage_bis_datum():
#     while True:
#         try:
#             # user input datum
#             datum_str = input("Bitte geben Sie ein Datum im Format TT.MM.JJJJ ein: ")

#             # stringer to datum
#             datum = datetime.strptime(datum_str, "%d.%m.%Y").date()

#             # today
#             heute = datetime.today().date()
#             print(f"{type (heute)}", heute)

#             # rechnen
#             differenz = (datum - heute).days
#             print(f"{type (differenz)}", differenz)

#             # output
#             print(f"Es sind {abs(differenz.days)} Tage von heute bis zum {datum_str}.")
#             break
#         except ValueError:
#             print("Ungültiges Datum. Bitte versuchen Sie es erneut.")


# tage_bis_datum()

# wochentag_berechnen()

# spieler_wahl = input("Deine Wahl: ").capitalize()
# print(f"{type spieler_wahl}", spieler_wahl)

# wochentag = [
#     "Montag",
#     "Dienstag",
#     "Mittwoch",
#     "Donnerstag",
#     "Freitag",
#     "Samstag",
#     "Sonntag",
# ]
# wochentag.pop(4)
# print(wochentag)

import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# 测试点
punkte = {0: (0, 0), 1: (3, 4), 2: (6, 8)}

# 手动计算点之间的距离
print("点 (0, 0) 和 (3, 4) 之间的距离:", distance(punkte[0], punkte[1]))  # 应该是 5
print("点 (0, 0) 和 (6, 8) 之间的距离:", distance(punkte[0], punkte[2]))  # 应该是 10
print("点 (3, 4) 和 (6, 8) 之间的距离:", distance(punkte[1], punkte[2]))  # 应该是 5

dist_matrix = [[distance(punkte[i], punkte[j]) for j in punkte] for i in punkte]

# 打印距离矩阵以验证

print("距离矩阵:")

for row in dist_matrix:
    print(row)

# allePunkt()
# 2. Rechnen alle punkte differenz
# def differenz(punkte):
# differenz = {}
# for t in range(16):
#     differenz[t] = punkte[t + 1][0] - punkte[t][0], punkte[t + 1][1] - punkte[t][1]
#     print(f"{differenz}")
# return differenz
