list1 = [2,6,4,9,7,20,1,8,34,22,11,56,3,5]

def linearsearch(list, targ):
  for i in range(len(list)):
    if list[i] == targ:
      return i
    #elif i != list[i]:
      #print('Not in list')
    else:
      i += 1
 
print(list1[-1])
print(linearsearch(list1, 9))
print(linearsearch(list1, 22))
print(linearsearch(list1, 8))
print(linearsearch(list1, 56))
print(linearsearch(list1, 3))
print(linearsearch(list1, 5))