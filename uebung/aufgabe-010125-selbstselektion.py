# Such Kurz Wege in 6 punkten


import random
import math
from itertools import permutations


# 1. Renden 6 punkte
def allePunkt():
    punkte = {}
    for i in range(6):
        punkte[i] = random.randint(1, 100), random.randint(1, 100)
        # print(f"{punkte}")
    return punkte


# 2. distance all points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


punkte = allePunkt()


dist_matrix = [
    [distance(punkte[i], punkte[j]) for j in range(len(punkte))]
    for i in range(len(punkte))
]
# print(dist_matrix)


# recht kurze wege
def total_distance(perm):
    return sum(dist_matrix[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))


# alle permutationen
perms = permutations(range(len(punkte)))

# finde kürzeste weg
min_perm = min(perms, key=total_distance)
shortest_distance = total_distance(min_perm)


print("alle punkte:", punkte)
print("kürzeste weg durch alle punkte:", min_perm)
print("distance:", shortest_distance)
