# # # x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

# # # num = int(input())
# # # if num in x:
# # #     print("bingo")

# # nums = list(range(5))
# # print(nums[4])

# def century(year):
#     if year % 100 == 0:
#         return year//100
#     elif year % 100 == 1:
#         return year
# print(century(1992))

def digitize(n):
    str_n = str(n) #Convert n to String
    new_n = []     #Create Empty list
    i = len(str_n)
    while i > 0:
        new_n.append(int(str_n[i-1]))
        print(i)
        i -= 1
    return new_n

print(digitize(59603))
