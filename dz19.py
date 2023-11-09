def common_elements():
    multiples_of_3 = set(range(3, 101, 3))
    multiples_of_5 = set(range(5, 101, 5))
    return multiples_of_3, multiples_of_5, multiples_of_3 & multiples_of_5

multiples_of_3, multiples_of_5, common_elements_set = common_elements()

print("Числа, кратні 3:", multiples_of_3)
print("Числа, кратні 5:", multiples_of_5)
print("Перетин:", common_elements_set)


