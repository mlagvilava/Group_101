#input ის მეშვეობით შემოვიტანოთ 2 სიტყვა და დაიპრინტოს, რომელსაც მეტი თანხმოვანი ექნება.
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

char1 = 0
char2 = 0

for char in name1:
    if char not in "aeiou":
        char1 += 1 

for char in name2:
    if char not in "aeiou":
        char2 += 1 

if char1 > char2:
    print("There are more consonants in the {}".format(name1))
elif char1 < char2:
    print("There are more consonants in the {}".format(name2))
else:
    print("Constants are equal")