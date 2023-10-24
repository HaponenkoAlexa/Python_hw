number = int(input("Введіть 4-х значне число: "))

digit_1 = number // 1000
digit_2 = (number % 1000) // 100
digit_3 = (number % 100) // 10
digit_4 = number % 10

print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)