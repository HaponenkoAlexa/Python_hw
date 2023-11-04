import keyword
import string

my_variable = input("Введіть змінну: ")

if len(my_variable) == 0 or my_variable[0].isdigit():
    print(False)
else:
    if not all(char in string.ascii_letters + string.digits + "_" for char in my_variable):
        print(False)
    elif my_variable in keyword.kwlist:
        print(False)
    else:
        print(True)
