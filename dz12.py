import string

my_hus = input('Введіть назву для хештега: ')
if my_hus:
    my_hus = ''.join(word.title() for word in my_hus.split() if word.isalpha())
    my_hus = f"#{my_hus}"
    my_hus = my_hus[:10]  # обмежуємо довжину хештега до 140 символів
    print(f"Ваш хештег: {my_hus}")
else:
    print("Ви ввели порожню строку.")



