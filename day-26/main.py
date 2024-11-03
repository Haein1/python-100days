
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#looping through dic
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through a data  frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print("-----")
    print(row)
    print(type(row))
    print(row.to_list())
    print(row.to_list()[0])

# list comprehension
# PyDev console: starting.
# Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32

# numbers = [1,2,3]
# new_numbers = [number+1 for number in numbers]
# print(new_numbers)
# [2, 3, 4]
# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)
# ['A', 'n', 'g', 'e', 'l', 'a']
# double_num = [2*num for num in range(1,5)]
# print(double_num)
# [2, 4, 6, 8]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# names
# ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [names for name in names if len(name)<=4]
# short_names
# [['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie'], ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie'], ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']]
# short_names = [name for name in names if len(name)<=4]
# short_names
# ['Alex', 'Beth', 'Dave']
# uppercase_names = [name.upper() for name in names if len(name)>5]
# uppercase_names
# ['CAROLINE', 'ELEANOR', 'FREDDIE']
#
#
#
# #dictionary
# names = ["Alex", " Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
#
# students_scores = {student:random.randint(100) for student in names}
# students_scores = {student:random.randint(0,100) for student in names}
# students_scores
# {'Alex': 3, ' Beth': 50, 'Caroline': 58, 'Dave': 99, 'Eleanor': 91, 'Freddie': 29}
# passed_students = {student:score for (student, score) in students_scores.items() if score>=60}
# passed_students
# {'Dave': 99, 'Eleanor': 91}
