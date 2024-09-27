#задача 2
try:
    number = int(input(" "))

    if number % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")
except ValueError:
    print("введи нормальное число гав гав гав")
