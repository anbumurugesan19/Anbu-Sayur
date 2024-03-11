# Homework-1:
# Remove duplicates

# case1
# Input: hellllllo | hello hello
# Output: helo  | helo


# def removeDuplicate(dup):
#     res = []
#     for i in dup : # It executes length of dup times
#         if i in res :
#             continue 
#         else : 
#             res.append(i)
#     return res


# dup = input("Enter any String : ")
# result = removeDuplicate(dup)
# print("Removed duplicates :",''.join(result))

# case2
# Input: hello hello | heLlo hello
# Output: helo helo | heLlo helo

# def removeDuplicate(word):
#     res = []
#     for char in word : # It executes length of dup times
#         if char not in res :
#             res.append(char)
#     return "".join(res)


# words = input("Enter any String : ").split()
# for word in words:
#     result = removeDuplicate(word)
#     print(result, end=" ")

# case3
# Input: heLlo helLo
# Output: helo helo 

# def removeDuplicate(word):
#     res = []
#     for char in word : # It executes length of dup times
#         if char not in res :
#             res.append(char)
#     return "".join(res)


# words = input("Enter any String : ").lower().split()
# for word in words:
#     result = removeDuplicate(word)
#     print(result, end=" ")


# Homework-2:
# Print your name in a pyramid
# Input: RAM
# Output:
# R
# RA
# RAM

# def pyramid(str):
#     length = len(str)
#     for row in range(length):
#         for col in range(row+1):
#             print(str[col], end=" ")
#         print()

# str = input("Enter a string: ")
# pyramid(str)

# Homework-3:
# Get an input string from the user. Add a space at every 3rd char.
# Input: abcdefwg
# Output: ab cd ef g 

str = "abcdefg"
newStr = ""

for i in range(0, len(str), 2):  # 0 2 4 6
    newStr += str[i:i+2]
    if i + 2 < len(str): # 2 < 7 | 4 < 7 | 6 < 7
        newStr += " "

print(newStr)

    



