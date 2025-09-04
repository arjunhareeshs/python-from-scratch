try:
    number = int(input())
    original = number
    soc = 0

    while number > 0:
        digit = number % 10
        soc += digit ** 3
        number = number // 10

    if original == soc:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
except ValueError:
    print("Invalid input")