#задача 3
try:
    number = int(input(" "))

    if 10 <= number <= 20:
        print("Число попадает в диапазон ")
    else:
        print("Число не попадает в диапазон")
except ValueError:
    print("введи нормальное число")
