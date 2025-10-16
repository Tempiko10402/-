def calculator():
    print("=== Простой калькулятор ===")
    print("Доступные операции: +, -, *, /")

    while True:
        try:
            a = float(input("Введите первое число: "))
            op = input("Введите операцию (+, -, *, /): ").strip()
            b = float(input("Введите второе число: "))

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = a / b
            else:
                print("Неизвестная операция!")
                continue

            print(f"Результат: {result}\n")

            again = input("Хотите продолжить? (д/н): ").lower()
            if again != 'д':
                print("Выход из калькулятора.")
                break

        except ValueError:
            print("Ошибка: введите корректные числа!\n")

calculator()
