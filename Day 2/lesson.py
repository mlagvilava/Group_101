name = "mamuka."    #string type varuable
age = 30            #int type varuable
height = 174.6      #float type varuable
true = True         #boolean type varuable


#if არის ლოგიკური ალტერნატივა პროგრამირებაში.
#თუ if ის მარჯვნივ დაწერილი პირობა True (ჭეშმარიტი) - ა მაშინ ქვევით დაწერილი კოდი შესრულდება.
#False (მცდარი) - ს შემთხვევაში არ შესრულდება.
if true:
    print("Say_Yes") #print_ის წინ ტაბია = 4 Space - ს. ამ გამოყოფას ქვია indentation.

if 5>10:            #ამ შემთხვევაში პირობა მცდარია
    print("_:(_")  #შესაბამისად ეს კოდიც არ შესრულდება.





print("Chemi saxelia {} da asaki {}".format(name, age)) #   
#Chemi Saxelia, da saki  ობიექტებია .format კი მეთოდი
#ხოლო  name და surname არგუმნტები, რომლებიც format მეთოდს გადაეცა.                                                  #

full_name = "mamuka lagvilava"
print(full_name[4:9])


name2 = "mamuka"
print(len(name2))


if "a" in full_name:
    print("gvxvdeba")


print(full_name[2:])
print(full_name[:6])
print(full_name[::3])


print(full_name[-1])

print(full_name.upper())

full_name2 = "MaMUKA LaGVILAVA"
print(full_name2.lower())
full_name3 = "     1 mamuka 2    "
print(full_name3.strip())

name = "nika"
print(name.replace("", "#"))