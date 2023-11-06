import string

my_hus = input('Введіть назву для хештега: ')
my_hus = my_hus.strip()[:140]
if my_hus:
    my_hus = ''.join(word.title() for word in my_hus.split() if word.isalpha())
    if all(char not in string.punctuation for char in my_hus):
        tmp = f"#{my_hus}"
        my_hus = tmp
        print(my_hus)
    else:
        print(False)
else:
    print("Ви ввели порожню строку.")

