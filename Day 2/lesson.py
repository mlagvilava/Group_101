name = "mamuka."    #string type varuable
age = 30            #int type varuable
height = 174.6      #float type varuable
true = True         #boolean type varuable


#if არის ლოგიკური ალტერნატივა პროგრამირებაში.
#თუ if ის მარჯვნივ დაწერილი პირობა True (ჭეშმარიტი) - ა მაშინ ქვევით დაწერილი კოდი შესრულდება.
#False (მცდარი) - ის შემთხვევაში არ შესრულდება.
if true:
    print("Say_Yes") #print_ის წინ ტაბია = 4 Space - ს. ამ გამოყოფას ქვია indentation.

if 5>10:            #ამ შემთხვევაში პირობა მცდარია
    print("_:(_")  #შესაბამისად ეს კოდიც არ შესრულდება.


print("Chemi saxelia {} da asaki {}".format(name, age)) #   
#Chemi Saxelia, da saki  ობიექტებია .format კი მეთოდი
#. - წერტილის მეშვეობით ობიექტებისთვის ხდება მეთოდების გამოძახება.
#ხოლო  name და surname არგუმნტებია, რომლებიც format მეთოდს გადაეცა.                                                  #

mokle___stringi = "hi"                #მოკლე String - ი იწერება 2 ბრჭყალში
grdzeli_stringi = """hi, rogor xar    #.........aq sul es tringia
ras shvebi........gamixarda.......    #.........aqac
...sheni naxva......ar daikargo"""    #გრძელი Sring - ი იწერება 6 ბრჭყალში (სამ-სამი) - სტილისტურად ასეა სწორი.
#პითნის გაიდლაინის მიხედვით 1 ხაზში(სტრიქონში) 80 სიმბოლოზე მეტი არ უნდა იყოს - Space (გამოტოვება) იც სიმბოლოა.

#შეგვიძლია არსებულ ობიექტებზე გამოვიძახოთ სხვადასხვანარი მეთოდები.
#ან არსებულ მეთოდებში გადავცეთ ეს ობიექტები.

#არსებულ name ობიექტზე გამოვიძახოთ ერთერთი მეთოდი.
print(name.capitalize()) #capitalize იგივე Uppercase - პირველი ასოს გადიდება.
#ყველა მეთოდს აქვს (მრგვალი ფრჩხილები)
#ზოგიერთ მეთოდს აქვს პარამეტრები ზოგიერთს არა. პარამეტრია (იგივე არგუმეტნი) რასაც (მრგვალ ფრჩხილში) გადავცემთ.

#pip install - ის მეშვეობით შეიძლება კონსოლიდან(ტერმინალიდან) ბიბლიოთეკების გადმოწერა/ინსტალაცია.

#ყველა სტრინგი შეიძლება აღიქვათ სიად.
#პროგრამირებაში ათვლა იწყება ნულიდან.
print(name[0]) #დაბეჭდავს n - ს.


full_name = "mamuka lagvilava"
print(full_name[4:9]) #დაბეჭდავს მე-4 ინდექსიდან (position) მე- 9 -მდე.

#ნებისმიერი სტრინგი შეიძლება ჩამოვჭრათ.

#მეთოდს გადავცეთ ობიექტი
name2 = "mamuka"
print(len(name2)) #len გამოიტანს name2 ობიექტის სიმბოლოების რაოდენობას.


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