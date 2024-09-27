try:
    num = float(input(" "))

    if num >= 0:
        if num > 0:
            print("Число положительное.")
        else:
            print("Число равно нулю.")
    else:
        print("Число отрицательное.")
except ValueError:
    print("другое число введи")
