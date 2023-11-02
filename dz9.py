import random
my_list = [random.randint(3, 10) for i in range(random.randint(1, 100))]
element_1 = my_list[0]
element_2 = my_list[2]
element_3 = my_list[-2]
result = [element_1, element_2, element_3]
print(my_list)
print(result)