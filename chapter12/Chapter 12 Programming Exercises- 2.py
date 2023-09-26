def recursive_multiply(x, y):
    if y == 1:
        return x
    else:
        return x + recursive_multiply(x, y-1)
x=int(input("please enter x:"))
y=int(input("please enter y:"))
print(recursive_multiply(x,y))