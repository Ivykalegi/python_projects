#with open("weather_data.csv") as data_file:
    # data = data_file.readlines()
    # print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) # object that can be looped through
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list)/len(temp_list)
# print(average)
#
# #get data in column
# print(data["condition"])
#
# #data in rows
# print(data[data.day == "Monday"] )#check for row where value == Monday
# print(data[data.temp == data.temp.max()])

# create a dataframe from scratch

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


df = data["Primary Fur Color"].value_counts()

df.to_csv("squirrel_count.csv")