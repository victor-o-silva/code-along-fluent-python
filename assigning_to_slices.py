my_list = list(range(10))
print(my_list)

my_list[2:5] = [20, 30]
print(my_list)

del my_list[5:7]
print(my_list)

my_list[3::3] = 11, 22
print(my_list)