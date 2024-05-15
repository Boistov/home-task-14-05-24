def translate(text):
    n = set()
    num = []
    for i in text:
        if i in n:
            num.append(f"{i}o{i}")
        else:
            num.append(i)
        n.add(i)
    return "".join(num)

a = input("Enter a string: ")
total = translate(a)
print(total)
