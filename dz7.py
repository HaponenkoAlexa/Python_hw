lst = [1, 0, 0, 3, 0, 7, 9, 7, 0,0, 0]
zero_count = lst.count(0)

lst = [x for x in lst if x != 0]

lst.extend([0] * zero_count)

print(lst)
