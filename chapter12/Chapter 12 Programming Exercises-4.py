def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    max_of_rest = find_max(lst[1:])
    if lst[0] > max_of_rest:
        return lst[0]
    else:
        return max_of_rest
x=int(input("please enter the fitst number in list-x:"))
y=int(input("please enter the second number in list-y:"))
z=int(input("please enter the third number in list-z:"))
u=int(input("please enter the fourth number in list-u:"))
v=int(input("please enter the fifth number in list-v:"))
list=[x,y,z,u,v]
print(find_max(list)) 