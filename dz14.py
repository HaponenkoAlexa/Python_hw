user_input = int(input("Введіть число: "))
product = 1
while user_input > 0 and product > 9:
    digit = user_input % 10
    product *= digit
    user_input = user_input // 10

print("Результат:", product)

