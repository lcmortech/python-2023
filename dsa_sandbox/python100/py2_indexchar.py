# Print the character at a specific index

# Write a python program that prints the character index at index i in the string str.
# If the index is out of range, the program should print "i is out of range"
# If the string is empty, the program should print "Empty String"

# def char_dex(str, char):
#     str_length = len(str)-1

#     for i in range(0, str_length):
#         if str == '':
#             return "Empty String"
#         elif i > len(str):
#             return "i is out of range"
#         elif str[i] == str[char]:
#             return str[char]
#     return str

# #test 
# test1 = 'happy'
# test2 = ''
# print(char_dex(test2, 1))

# Solution 2

# def char_dex(str, char):
#     str_length = len(str)-1

#     for i in range(0, str_length):
#         if str[i] == str[char]:
#             return str[char]
#         elif i < len(str):
#             return "i is out of range"
#         else:
#             return "Empty String"


# Actual Solution

def char_dex(str, char):
    str_length = len(str)-1

    for i in range(0, str_length):
        if len(str) == 0:
            return "Empty String"
        elif i < len(str):
            return str[i]
        else:
            return "i is out of range"


#test
test = char_dex('book', 3)
print(test)
        
