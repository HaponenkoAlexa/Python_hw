number = int(input("Введіть кількість секунд: "))

if 0 <= number <= 8640000:
    days, seconds = divmod(number, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days == 0:
        day_word = "днів"
    elif days == 1:
        day_word = "день"
    elif days // 10 == 1 or days % 10 in (2, 3, 4):
        day_word = "дні"
    else:
        day_word = "днів"

    formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(formatted_time)
else:
    print(False)

