# a = ["a", "b", "c", "d"]
# b = [1, 2, 3, 4]
# c = ["d", "c", "b", "a"]
# d = []
# i = 0
# while i < len(a):
#     d.append(a[i])
#     d.append(b[i])
#     d.append(c[i])
#     i+=1
# print(d)

def zipp (a, b, c):
    d = []
    result = ""
    i = 0
    while i < len(a):
        d.append(a[i])
        d.append(b[i])
        d.append(c[i])
        i+=1
    return d

a = ["a", "b", "c", "d"]
b = [1, 2, 3, 4]
c = ["d", "c", "b", "a"]

print(zipp(a, b, c))