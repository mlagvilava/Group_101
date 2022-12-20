# sawmelebi = ["vashli", "banani", "pomidori", "wiwibura", "shaurma"]
# arajansagi_sawmelebi = ['shaurma', 'burgeri', 'hot dogi', 'pica']
# for sawmeli in sawmelebi:
#       if sawmeli in arajansagi_sawmelebi:
#             continue
#       else:
#             print(sawmeli)


# def count_sheep(n):
#     i = 1
#     sheep_str = ""
#     while i != n + 1:
#         sheep_str += str(i) + " sheep..."
#         i += 1
#     return sheep_str

# print(count_sheep(1))

# def rps(p1, p2):
#     winner_combo = {
#         "rock": "scissors",
#         "scissors": "paper",
#         "paper": "rock"
#     }
      
#       if winner_combo[p1] == (p2):
#       return "Player 1 won!"


# print(rps('rock', 'scissors'))
# print(rps('scissors', 'paper'))

# def get_grade(s1, s2, s3):
#     average =  95 #(s1 + s2 + s3) / 3
#     print(type(average))
#     if average >= 90 and average <= 100:
#         return "A"
#     elif average <= 80 and average <= 90:
#         return "B"
    
# print(get_grade(95, 90, 93))

# def quarter_of(month):
#     if month <= 3:
#         return "1"
#     elif 3 < month <= 6:
#         return "2"
#     elif 6 < month < 9:
#         return "3"
#     elif 9 < month <= 12:
#         return "4"


# print(quarter_of(4))

# def switch_it_up(number):
#     dictionary_nums =  {
#         0: "Zero",
#         1: "One",
#         2: "Two",
#         3: "Three",
#         4: "Four",
#         5: "Five",
#         6: "Six",
#         7: "Seven",
#         8: "Eight",
#         9: "Nine"
#         }
#     return dictionary_nums[number]

#     thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# def to_alternating_case(string):
#     string_arr = []
#     modified_string = ""
#     for char in string:
#         string_arr.append(char)
#     for char in string_arr:
#         if char == char.upper():
#             modified_string += char.lower()
#         elif char == char.lower():
#             modified_string += char.upper()
#     return modified_string

# print(to_alternating_case("hoPla biy aAaA"))


# def to_alternating_case(string):
#     new_str = ''
#     for char in string:
#         if char.isupper():
#             new_str += char.lower()
#         else:
#             new_str += char.upper()
#     return new_str

# print(to_alternating_case("AakOpopoaA asdA A"))

# def to_alternating_case(string):
#     new_




def to_alternating_case (string):
    new_string = ""
    for char in string:
        if char == char.lower():
            new_string= new_string + char.upper()
        elif char == char.upper():
            new_string = new_string + char.lower() 
    return new_string

print(to_alternating_case("AAA AAAA AAA"))