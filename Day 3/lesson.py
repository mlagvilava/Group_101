# g1 = input("pirveli cifri: ")
# g2 = input("meore cifri: ")

# print(int(g1)+int(g2))

# num1 = int(input("enter number1: "))
# num2 = int(input("enter number2: "))
# num3 = num1 * num2

# if num3 > int("100"):
#     print("xxx")
# else:
#     print("yyy")

# a = 3
# b = 6

# print(a + b)
# print(a * b)
# print(a / b)
# print(a - b)

# print(b % a) #რამდენი დარჩება ნაშტი გაყოის შემდეგ
# print(a ** b) #ხარისხში აყვანა
# print(a//b) #ორმაგი გაყოფა, ანუ გაყოფს და Float ს გადაიყვანს Integer ში.

from lib2to3.pgen2.token import EQUAL


num1 = int(input("First number"))
num2 = int(input("Second number"))
num3 = int(input("Third number"))

num_1 = num1 % 2
num_2 = num2 % 2
num_3 = num3 % 2

if num_1 > 0:
    num1 = num1
else:
    num1 = 0

if num_2 > 0:
    num2 = num2
else:
    num2 = 0

if num_3 > 0:
    num3 = num3
else:
    num3 = 0

print(num1 + num2 + num3)