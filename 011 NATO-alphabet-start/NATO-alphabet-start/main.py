# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# for(index, row) in data.iterrows():
#     # print(index)
#     # print(row)
#     print(row.to_list()[0])
#     print(row.to_list()[1])

data_dic = {row.to_list()[0] : row.to_list()[1] for (index, row) in data.iterrows()}
# print(data_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word:")
user_code = []
for l in user_input:
    if l.upper() in data_dic.keys():
        user_code.append(data_dic[l.upper()])

print(user_code)