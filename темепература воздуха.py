temp = float(input("Введите температуру воздуха : "))

if temp <= -20:
    print("Очень холодно")
elif -20 < temp <= 0:
    print("Холодно ")
elif 0 < temp <= 10:
    print("Прохладно")
elif 10 < temp <= 20:
    print("Тепло")
elif 20 < temp <= 30:
    print("Жарко")
else:
    print("Очень жарко")
