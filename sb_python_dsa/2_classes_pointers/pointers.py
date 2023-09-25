num1 = 11
num2 = num1

#print(num2)

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
#num1 points to: 9793408
#num2 points to: 9793408

num2 = 22
print(num1, num2)

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
#num1 points to: 9793408
#num2 points to: 9793760

# Integers (like 11) are immutable in memory; they cannot be changed

dict1 = {
    'value':11
}

dict2 = dict1

print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print(dict1, dict2)
dict2['value'] = 22
print(dict1, dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
# dict1 points to: 139672965828544
#dict2 points to: 139672965828544

# dictionaries are not immutable and CAN be changed (needed later for linked list, which operates similarly)
#ll: if you have two variables that point at the same node you can change the value of that node and the variables will continue to point to the same node even though we changed the value

# all three variables pointing at the same node, python removes unaccessible variable through a process known as garbage collection