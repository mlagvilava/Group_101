my_list = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali"]
prices = [2, 20, 15, 10, 15, 2]

i = 0
while i < len(my_list):
    # print(my_list[i] + " girs " + str(prices[i]) + " lari")
    print(my_list[i]," girs ",prices[i]," lari") #თუ + ის ნაცვლად გამოვიყენებთ მძიმეს მაშინ 
                                                 #str ით კონვერტაცია არ გვჭირდება თვითონ იზამს.
    i += 1


my_array = ["banana", 11, True, 10.5, [1,2,3]] # სია პითონში შეძლება შედგებოდეს სხვადასხვა ტიპის ელემენტებისგან
 #სხვა ენებში ასე ვერ ვიზამთ.
 #int prices = [2, 20, 15, 10, 15, 2] java 
 #კვადრატილი ფრჩხილით შექმნილი კოლექცია არის list - კოლექცია ელემეტების მიმდევრობაა.

print(my_array[-1]) # დაპრინტავს ბოლო ელემენტს
print(my_array[3])  # დაპრინტავს მე-3 პოზიციაზე მდგომს
print(my_array[1:3])   # დაპრინტავს 1 იდან 3 მდე.
print(my_array[0:4:2]) # დაპრინტავს 0 დან 4 მდე 2 ის გამოტოვებით.
print(my_array[:4])    # დასაწყისიდან მე-4 მდე.



menu = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali"]
# if "lobiani" in menu:
#     print("lobiani gvaqvs")
menu[1] = "BBQ" # menu სიაში 1 პოზიციაზე მდგომ ელემენტს ვანაცვლებთ BBQ თ.
menu[2:4] = ["aa", "bb", "cc"] #ჩავანაცვლეთ დიაპაზონი.
print(menu)

#სტრინგის შემთხვევაში
my_name = "mamuka"
new_name = ""

for i in range(len(my_name)):
    if i == 2 or i ==3:
        new_name += "q"
    else:
        new_name += my_name[i]
print(new_name)
#ან
print(my_name.replace("uk", "qq"))
#ზოგჯერ ჯობია გამოვიყენოთ ჩვენი შექმნილი ხერხები ვიდრე მზა მეთოდები.

menu = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali"]
menu.insert(3, "nayini")
print(menu)

# #davaleba
# # momxmarebel shemoaqvs 5 sachmeli
# # siashi sheitanet isini romlebic sheicaven minimum 2 a - s.


# menu = []
# a = 0
# i = 0
# while i < 6:
#     food = input("Type Food Name:")
#     for a in food:
#         a += 1
#     if a > 1:
#         menu.append(food)
#     i += 1
# print(menu)