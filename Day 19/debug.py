def zipp (a, b, c):
    d = []
    result = ""
    i = 0
    while i < len(a):
        result = a[i] + str(b[i]) + c[i]
        i+=1
        d.append(result)
    return d

a = ["a", "b", "c", "d"]
b = [1, 2, 3, 4]
c = ["z", "x", "y", "w"]

print(zipp(a, b, c))

#['a', 1, 'z', 'b', 2, 'x', 'c', 3, 'y', 'd', 4, 'w']