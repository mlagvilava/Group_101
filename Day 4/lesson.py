# # # პროგრამირებაში არის ციკლები და იტერაციები.
# # my_name = "mamuka"

# # for char in my_name:    # char აირს საიტერაციო ცვლადი, რომელიც ციკლის განმავლობაში იცვლის მნიშვნელობას.
# #     print(char)         # iteration ნიშნავს განმეორებას.

# # print (3 + 3)


# x = input()
# y = input()
# print = (x * int(y))

# total = 0
# #aba midi
# tkt = 100
# p1 = int(input())
# p2 = int(input())
# p3 = int(input())
# p4 = int(input())
# p5 = int(input())

# for i in (p1, p2, p3 ,p4 ,p5):
#     if i <= 3:
#         i = 0
#     else:
#         i = 100
#     total += i

# print(total)

#your code goes here
weight = int(input())
height = float(input())

bmi = weight/height ** 2
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30:
    print("Obesity")