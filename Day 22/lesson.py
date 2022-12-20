def odd_count(n):
    if n%2 == 1:
        return n // 2
    elif n%2 == 0:
        return (n // 2) - 1

print(odd_count(10))