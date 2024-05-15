
def san_j(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = ["a", "b"],["c", "d"]
list2 = ["e", "f"], ["a", "h"]

num = san_j(list1, list2)
print(num)
