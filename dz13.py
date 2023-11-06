import string

input_str = input("Введіть дві літери через дефіс (наприклад, a-c): ")
first_letter, second_letter = input_str.split('-')

min_pos = string.ascii_letters.index(first_letter)
max_pos = string.ascii_letters.index(second_letter)

result = string.ascii_letters[min_pos:max_pos + 1]
print(result)


