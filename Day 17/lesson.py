#abs ფუნქცია პოულობს მანძილს რიცხვიდან ნულამდე.
#dictionary

# my_students = {
#     "luka": 18,
#     "nika": 24,
#     "sandro": 20,
#     "mzia": 46
#     #key:value
# #amis ჰორიზონტალურად წერა სტილისტურად არასწორია.
# }
# print(my_students["nika"])

# my_students = {
#     "luka": 18,
#     "nika": 20,
#     "sandro": 30,
#     "mzia": 46
# }

# my_students["nika"] = 5
# print(my_students)
# print(my_students.get("mzia"))

# print(list(my_students.items()))
# print(list(my_students.items())[0][1])

# print(list(my_students.keys()))
# print(list(my_students.values()))
# print(my_students.pop("mzia"))

# list = [[1, 1], [2, 3], [5, 8, 2]]
# print(list[list[2][list[1][0]]])

# print(list[1][0])
# print(list[2][2])
# print(list[2])

# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squares[::2])
# print(squares[2:8:3])
# print(squares[:2])

#"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
def reverse_words(s):
    temp_arr = []
    temp_arr = s.split()
    return s

s = "The greatest victory is that which requires no battle"
print(reverse_words(s))