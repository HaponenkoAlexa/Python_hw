import string

my_hus = input('Введіть назву для хештега: ')
if my_hus:
    my_hus = ''.join(word.title() for word in my_hus.split() if word.isalpha())
    if all(char not in string.punctuation for char in my_hus):
        tmp = f"#{my_hus.strip()[:140]}"
        my_hus = tmp
        print(f"Ваш хештег: {my_hus}")
    else:
        print("Хештег не може містити символи пунктуації, будь ласка, введіть іншу назву.")
else:
    print("Ви ввели порожню строку.")


