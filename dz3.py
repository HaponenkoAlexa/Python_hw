number = int(input("Введіть п'ятизначне число: "))

digit_1 = number // 10000
digit_2 = (number % 10000) // 1000
digit_3 = (number % 1000) // 100
digit_4 = (number % 100) // 10
digit_5 = number % 10


print(digit_5, digit_4, digit_3, digit_2, digit_1, )