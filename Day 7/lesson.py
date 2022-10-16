#davaleba
# momxmarebel shemoaqvs 5 sachmeli
# siashi sheitanet isini romlebic sheicaven minimum 2 a - s.
from re import A


menu = []
a = 0
i = 0
while i < 6:
    food = input("Type Food Name:")
    for a in food:
        a += 1
    if a > 1:
        menu.append(food)
    i += 1
print(menu)