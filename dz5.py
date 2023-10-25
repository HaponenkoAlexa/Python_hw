my_list = [ 3,5,6]
if len(my_list) == 0:
    print([[], []])
elif len(my_list) % 2 == 0:
    middle = len(my_list) // 2
    first_half = my_list[:middle]
    second_half = my_list[middle:]
    print([first_half, second_half])
else:
    middle = len(my_list) // 2
    first_half = my_list[:middle + 1]
    second_half = my_list[middle + 1:]
    print([first_half, second_half])