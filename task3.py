def is_number(x, a):
    for item in a:
        if item == x:
            return True
    return False

list1 = input()
a = input()
b = input()

result = is_number(a,list1)

print(result)