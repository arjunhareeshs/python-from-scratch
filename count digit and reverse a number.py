a = int(input("Enter a number"))
cake = 0
reverse_number = 0
while a!=0:
    reverse_number = reverse_number * 10 + (a%10)
    a = a // 10
    cake += 1
print(cake)
print(reverse_number)

