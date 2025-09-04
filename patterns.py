rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1): 
        print("*", end=" ")  
    print()
    
teeks = int(input("Enter the row size for the pattern: "))
for i in range(teeks, 0, -1): 
    for j in range(1, i + 1): 
        print("*", end=" ") 
    print()
    
rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1): 
    for j in range(rows  - i):
        print(" ", end=" ")
    for k in range(1, 2 * i): 
        print("*", end=" ")
    print()
    
rows = int(input("Enter the row size for the pattern: "))
for i in range(rows , 0, -1):
    for j in range(rows  - i): 
        print(" ", end=" ")
    for k in range(1, 2 * i): 
        print("*", end=" ")
    print() 
    
rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1): 
    for j in range(1, rows + 1): 
        if i == 1 or i == rows or j == 1 or j == rows :  
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()