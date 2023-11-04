while True:
    x = int(input("Введіть число: "))
    action = input('Введіть дію (+, -, *, /): ')
    z = int(input("Введіть число: "))

    if action == "+":
        result = x + z
    elif action == "-":
        result = x - z
    elif action == "*":
        result = x * z
    elif action == "/":
        if z != 0:
            result = x / z
        else:
            print("Ділення на нуль неможливе.")
            result = None

    if result is not None:
        print("Результат:", result)
        reply = input('Хочете продовжити? Введіть "Так" або "Ні": ')
        if reply.lower() != 'так':
            print("Завершення")
            break


