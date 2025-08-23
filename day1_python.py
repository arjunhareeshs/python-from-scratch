#getting input from the user and printing it
Int = int(input())
Float = float(input())
String = input()
print(Int)
print(Float)
print(String)

listt = list(map(int, input().split()))
print(listt)
tuuple = tuple(map(int, input().split()))
print(tuuple)

for l in listt:
    if(l%2==0):
        print(l)
    else:
        print(-1)

print(l if l%2 == 0 else -1 for l in tuple)

choice = int(input())

match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid")

