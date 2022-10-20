#def წინა დავალებებისგან შევქმნათ ფუნქციები.
# print max number from list
# def maxnum(scores):
#     max_vol = 0
#     for score in scores:
#         if score > max_vol:
#             max_vol = score
#     print(max_vol)

# scores = [60, 90, 50, 100, 50000]
# maxnum(scores)
#------------------------------------
# reverse list
# def listrev(students):
#     new_list = []
#     i = len(students)
#     while i > 0:
#         new_list.append(students[i-1])
#         i -= 1
#     print(new_list)

# students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "farna"]
# listrev(students)
#-----------------------------------
#menu & price
# def menu(my_list, prices):
#     i = 0
#     while i < len(my_list):
#         print(my_list[i], " girs ", prices[i], " lari")
#         i += 1
# my_list = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali"]
# prices = [2, 20, 15, 10, 15,2]
# menu(my_list, prices)
#-----------------------------------
#print vovels and index from string
# def vow_index(name):
#     i = 0
#     while i < len(name):
#         if name[i] in "aeiou":
#             print(i, name[i])
#         i += 1

# name = input()
# vow_index(name)
#----------------------------------
#print name with more vowels
# def max_vowel(name1, name2):
#     char1 = 0
#     char2 = 0
#     for i in name1:
#         if i in "aeiou":
#             char1 += 1
#     for x in name2:
#         if x in "aeiou":
#             char2 += 1
#     if char1 > char2:
#         print(name1 + " has more vowels")
#     elif char1 < char2:
#         print(name2 + " has more vowels")
#     else:
#         print(name1 + " and " + name2 + " have the same number of vowels")

# name1 = input()
# name2 = input()
# max_vowel(name1, name2)
#-----------------------------------
#take numbers from input and sum only evens
def oven_sum(num1, num2, num3):
    sum = 0
    if num1 % 2 > 0:
        sum += num1
    if num2 % 2 > 0:
        sum += num2
    if num3 % 2 > 0:
        sum += num3
    print(sum)

num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))
num3 = int(input("Enter Third Number"))

oven_sum(num1, num2, num3)