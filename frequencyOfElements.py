list = [1, 4, 6, 8, 3, 4, 5, 6, 7, 8, 6, 5, 2]

x_count = 0
y_count = 0

print(set(list))
for num in range(len(list)):
    print("{} appears {} times".format(list[num], list.count(list[num])))