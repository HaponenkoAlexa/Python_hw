number = int(input("Введіть кількість секунд: "))

if 0 <= number <= 8640000:
    days, seconds = divmod(number, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    formatted_time = f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(formatted_time)
else:
    print(False)
