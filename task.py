def digits(n):
    a = str(n)
    for a in a:
        if int(a) % 2 == 0:
            return False

    return True

number = int(input("Enter: "))
num = digits(number)

print(num)
























