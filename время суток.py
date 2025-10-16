hour = int(input("Введите час (от 0 до 23): "))

if hour < 0 or hour > 23:
    print("Ошибка: час должен быть от 0 до 23.")
else:
    if 0 <= hour < 6:
        print("Ночь")
    elif 6 <= hour < 12:
        print("Утро")
    elif 12 <= hour < 18:
        print("День")
    else:
        print("Вечер")
