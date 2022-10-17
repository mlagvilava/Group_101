# scores = [20, 43, 56, 73, 10, 6, 87, 45, 97]
# high_score = 0

# for x in scores:
#     for i in scores:
#         if x > i:
#             high_score = x
#             i = x
#             print(str(x) + " it\'s is x")
#         elif x < i:
#             hight_score = i
#             x = i
#             print(str(i) + " it\'s is i")

# print(str(high_score) + " it\'s literaly hard for me")

#-----------------------------------------------------

#ორ რიცხვს შორის უდიდესს ანიჭებს max_vol ცვლადს და ცილკის მეშვეობით 
#აგრძელებს შედარების პროცესს მარჯვნივ მდგომ რიცხვთან.
#შედარების შედეგი ყოველ ჯერზე გამოაქვს ტერმინალში - თვალსაჩინობისთვის.
# scores = [20, 43, 56, 73, 10, 6, 87, 45, 97]
# max_vol = 0
# i = 0
# while i+1 < len(scores): #სანამ i+1 არ დავწერე 27-ე ხაზზე აგდებდა შეცდომას Out of range
#     x = i + 1
#     if scores[i] > scores[x]:
#         max_vol = scores[i]
#         print(str(max_vol) + " Metia " + str(scores[x]) + "-ze")
#     else:
#         max_vol = scores[x]
#         print(str(scores[i]) + " Naklebia " + str(max_vol) + "-ze")
#     i += 1

#-----------------------------------------------------
#სიის შეტრიალება.
students = ["nika", "ana", "mamuka", "beqa", "dachi", "iva", "farna"]
new_list = students[::-1]
print(new_list)