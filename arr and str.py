lis = list(map(int, input().split()))
print(lis)
t = tuple(map(int, input().split()))
print(t)
for i in lis:
    if i % 2 == 0:              # all command line are written by me
        print(i)
    else:
        print(-1)
print(i if i % 2 == 0 else -1 for i in t)  #another method to do the same thing

str = input("enter a string: ")
print(str)
#string slicing
print(str[::-1])  #to reverse a string this comment is written by me
print(str[::2])   #to print alternate characters in a string

for tokens in str.split():
    print(tokens)
for tokens in str:
    print(tokens ,end = ' ')
print()
#appending strings
str = str + " is a good boy"
print(str)