#კონსოლიდან შემოდის 3 ციფრი
#აქედან იპრინტება მხოლოდ კენტების ჯამი

num1 = int(input("First number"))
num2 = int(input("Second number"))
num3 = int(input("Third number"))

if num1 % 2 > 0:
    num1 = num1
else:
    num1 = 0

if num2 % 2 > 0:
    num2 = num2
else:
    num2 = 0

if num3 % 2 > 0:
    num3 = num3
else:
    num3 = 0

print(num1 + num2 + num3)