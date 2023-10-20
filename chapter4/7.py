salary = 0
days = int(input('Pleass enter the number of days:'))
x = 1
for a in range(1,days + 1):
    salary += x
    print('Salary:' , x/100, 'in day', a)
    x *= 2
print('The total salary is:', salary/100)
