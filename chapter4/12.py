def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a nonnegative integer: "))
if number < 0:
    print("The entered number should be nonnegative.")
else:
    fact = factorial(number)
    print(f"{number}! = {fact}")