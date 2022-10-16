scores = [20, 43, 56, 73, 10, 6, 87, 45, 97]
high_score = 0

for x in scores:
    for i in scores:
        if x > i:
            high_score = x
            i = x
            print(str(x) + " it\'s is x")
        elif x < i:
            hight_score = i
            x = i
            print(str(i) + " it\'s is i")

print(str(high_score) + " it\'s literaly hard for me")

#-----------------------------------------------------

# scores = [20, 43, 56, 73, 10, 6, 87, 45, 97]
# scor1 = scores[0::2]
# scor2 = scores[1::2]
# i = 0
# while i < len(scores):
#     if scores[:i:] > scores[i:2:2]:
#         print(i)
#     i += 1
# # print(scores[:1:] < scores[1:2:2])
# # print(scores[:1:])
# # print(scores[1:2:2])
