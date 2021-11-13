# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     print(value)
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(row)
#
# # Keyword Method with iterrows()
# new_dict = {row.student:row.score for (index, row) in student_data_frame.iterrows()}
# print(new_dict)


import pandas
#
# #TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_data_frame = pandas.DataFrame(nato_alphabet)
# print(nato_data_frame)

# create dictionary from nato_data_frame

new_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
# print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("what is the word?").upper()
phonetic_list = [new_dict[letter] for letter in word]
print(phonetic_list)