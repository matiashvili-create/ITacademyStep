while True:
    try:
        height = int(input("შეიყვანეთ პირამიდის სიმაღლე (1-8): "))

        if 1 <= height <= 8:
            break
        else:
            print("გთხოვთ შეიყვანოთ რიცხვი 1-დან 8-ის ჩათვლით.")

    except ValueError:
        print("გთხოვთ შეიყვანოთ მთელი რიცხვი!")

for i in range(1, height + 1):

    for j in range(height - i):
        print(" ", end="")

    for k in range(i):
        print("#", end="")

    print()