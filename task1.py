#задача 1
try:
    number = float(input())

    if number > 0:
        print("Число положительное")
    else:
        print("Число не положительное")
except ValueError:
    print("инвалид чтоли? введи число")
