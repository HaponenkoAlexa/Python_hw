import string
import keyword

my_variable = input("Введіть змінну: ")

if len(my_variable) == 0:
    print(False)
elif my_variable == "_":
    print(True)
elif my_variable[0].isdigit() or not my_variable.islower():
    print(False)
elif not all(char in string.ascii_letters + string.digits + "_" for char in my_variable):
    print(False)
elif my_variable in keyword.kwlist:
    print(False)
else:
    print(True)
