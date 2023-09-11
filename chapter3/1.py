num = int(input("please enter an integer: "))


if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")