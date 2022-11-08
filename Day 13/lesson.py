# def past(h, m, s):
#     ms_in_s = 1000
#     ms_in_m = 60000
#     ms_in_h = 3600000
#     ms = 0
#     return h*ms_in_h + m*ms_in_m + s*ms_in_s

# print(past(1, 1, 1))

# def invert(lst):
#     new_lst = []
#     for i in lst:
#         if i < 0:
#             new_lst.append(i)
#         elif i > 0:
#             new_lst.append(i * -1)
#     return(new_lst)
# lst = [-1, 2, 3, 6]
# print(invert(lst))

# def fake_bin(x):
#     new_x = ""
#     for element in x:
#         if int(element) < 5:
#             new_x += "0"
#         elif int(element) > 5:
#             new_x += "1"
#     return new_x

# x = [1, 4, 7, 8]
# print(fake_bin(x))

def calc_age(age):
	return age * 365

print(calc_age(65))