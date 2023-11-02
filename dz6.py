my_list = []

if my_list:
    last_element = my_list.pop()
    my_list.insert(0, last_element)
    print(my_list)
else:
    my_list = []
    print(my_list)


