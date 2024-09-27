#задание 4
try:
    num1 = float(input(" "))
    num2 = float(input(" "))
    if num1 > 10 and num2 > 10:
        print("Оба числа больше 10.")
    else:
        print("Одно или оба числа не больше 10.")
except ValueError:
    print("Пожалуйста, введите корректные числа.")
