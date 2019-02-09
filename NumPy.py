import numpy as np

num_dict = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10 : 0,
    11 : 0,
    12 : 0,
    13 : 0,
    14 : 0,
    15 : 0,
    16 : 0,
    17 : 0,
    18 : 0,
    19 : 0,
    20 : 0
}

count = 0

vector = np.random.randint(20, size=15)

print(vector)

for x in vector:
    if x not in num_dict :
        num_dict[x] = 1
    else:
        num_dict[x] += 1
print('')
print(num_dict)
biggest = num_dict[1]

for key in num_dict:
    if num_dict[key] > biggest:
        biggest = key

print('')
print("Most freqent number(s): ", biggest)