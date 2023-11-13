number = int(input("Введіть кількість секунд: "))

if 0 <= number <= 8640000:
    days, seconds = divmod(number, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days == 0:
        day_word = "днів"
    elif days == 1 or (days % 10 == 1 and days % 100 != 11):
        day_word = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "дні"
    else:
        day_word = "днів"

    formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(formatted_time)
else:
    print(False)

