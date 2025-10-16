import random

print("=== Игра: Угадай число от 1 до 5 ===")

secret_number = random.randint(1, 5)

guess = int(input("Введите число от 1 до 5: "))

if guess == secret_number:
    print(f"Поздравляю! Вы угадали! Это число {secret_number}.")
else:
    print(f"Не угадали. Было загадано число {secret_number}.")
