my_list = [1,22,44]

if len(my_list) == 0:
    print(my_list)
else:
    sum_of_even_indices = sum(my_list[::2])
    if len(my_list) > 0:
        last_element = my_list[-1]
        result = sum_of_even_indices * last_element
        print(result)
