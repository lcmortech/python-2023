list1 = [2,6,4,9,7,20,1,8,34,22,11,56,3,5]

def linearsearch(list, targ):
  for i in range(len(list)):
    if list[i] == targ:
      return i
    elif i != list[i]:
      i += 1
    else:
      print('Not in list')
 
print(list1[-1])
print(linearsearch(list1, 9))
print(linearsearch(list1, 22))
print(linearsearch(list1, 8))
print(linearsearch(list1, 56))
print(linearsearch(list1, 51))
print(linearsearch(list1, 3))
print(linearsearch(list1, 5))

# Runtime: O(n)