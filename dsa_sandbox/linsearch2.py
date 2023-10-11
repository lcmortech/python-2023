list2 = [2,6,4,9,7,20,1,8,34,22,11,56,3,5]

def linearsearch2(list, targ):
    searchMap = {}

    for i, n in enumerate(list):
        if n == targ:
            return i
        elif n != targ:
            i += 1
        else:
            return "Not in list"

print(list2[-1])
print(linearsearch2(list2, 9))
print(linearsearch2(list2, 22))
print(linearsearch2(list2, 8))
print(linearsearch2(list2, 56))
print(linearsearch2(list2, 51))
print(linearsearch2(list2, 3))
print(linearsearch2(list2, 5))