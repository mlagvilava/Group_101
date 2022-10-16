full_name = input()

# for i in name:
#     if i in "aeiou":
#         print(i)

i = 0
while i < len(full_name):
    if full_name[i] in "aeiou":
        print(str(i) + full_name[i])
    i += 1