#def last_number(a, b, c):
#    return (a * b) % 10 == c % 10

#a = 1
#b = 2
#c = 2
#print(last_number(a, b, c))
































#def last_number(a, b, c):
#    if a == 0 or b == 0:
#        return a * b == c

#    if a * b == c:
#        return last_number(a // 10, b // 10, c // 10)
#    else:
#        return False
#a = input()
#b = input()
#c = input()
#print(last_digit_match(a, b, c))
















def even_number(num):
    i = 0
    n = []
    while i < len(num):
        if num[i] % 2 == 0:
            n.append(num[i])
        i += 1
    print(i)

numbers = [55, 43, 7, 23, 5, 6,]
javob = even_number(numbers)
print(javob)
