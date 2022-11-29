#ეს ფუნქცია აბრუნებს  უდიდეს და უმცირეს
#სიათა ელემენტების რაოდენობის სხვაობას და
#უდიდეს სიას
def get_max (a, b, c):
    A = [len(a), a]
    B = [len(b), b]
    C = [len(c), c]
    meti = []
    if A[0] > B[0] and A[0] > C[0]:
        meti.append(A[0] - B[0])
        meti.append(A[1])
    elif B[0] > A[0] and B[0] > C[0]:
        meti.append(B[0] - A[0])
        meti.append(B[1])
    elif C[0] > A[0]  and C[0] > B[0]:
        meti.append(C[0] - A[0])
        meti.append(C[1])
    return meti
#ფუნქციის დასასრული

#მე-2 ფუნქცია
def zipp (a, b, c):
    d = []
    i = 0
    min_len = min(len(a), len(b), len(c))
    while i < min_len:
        result = a[i] + str(b[i]) + c[i]
        i+=1
        d.append(result)
    d.append((get_max(a, b, c)[1])[(get_max(a, b, c))[0]:]) # აქ ვიძახებ პირველ get_max(a, b, c) ფუნქციას, რომელიც აბრუნებს სიას 2 ელემენტით (უდიდესი სიის დასახელებას და ელემენტთა რაოდენობის სხვაობას უმცირეს სიასთან)
    return d
#მე-2 ფუნქციის დასასრული

#test case
a = ["a", "b", "c", "d"]
b = [ 1,   2,   3,   4 ]
c = ["z", "x", "y", "w", "h", "q", "y"]

print(zipp(a, b, c))