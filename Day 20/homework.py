# #1 1000 100 000
# #1 60   3600

# def cockroach_speed(s):
#     return (s * 100000) // 3600    


# print(cockroach_speed(1.08))


# def monkey_count(n):
#     new_n = []
#     i = 0
#     while i != 5:
#         new_n.append(i +1)
#         i += 1
#     return new_n

# print(monkey_count(5)[-1])


# def update_light(current):
#     color = ["green", "yellow", "red"]

#     if current in color:
#         return color[color.index(current) -1]

# print(update_light('green'))


# def first_non_consecutive(arr):
#     for num in arr:
#         if arr[num] - num != 1:
#             return arr[num]

# def first_non_consecutive(arr):

#     i = len(arr) - 1
#     while i > 0:
#         if arr[i] - arr[i - 1] > 1:
#             return arr[i]
#         i -= 1

# def first_non_consecutive(arr):
#     i = 0
#     while i < len(arr):
#         if arr[i] - arr[i - 1] > 1:
#             return arr[i]
#         i += 1

# print(first_non_consecutive([1,3,4,6,7,8]))
# print(first_non_consecutive([1,2,3,4,5,6,7,8]))


def count_sheep(n):
    i = 0
    arr = []
    while i < n:
        if i < 1:
            return "555"
        elif i >= 1:
            arr.append((str(i) + " sheep..."))
        i += 1
    return "".join(arr)

print(count_sheep(5))