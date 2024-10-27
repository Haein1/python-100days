import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241027.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict = {"Fur Color": ["gray", "red", "black"],
             "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]}

# print(data_dict)
csv_data = pandas.DataFrame(data_dict).to_csv("squirrel_count.csv")

# index = pandas.Index(["Gray", "Cinnamon", "Black", data["Primary Fur Color"]])
# #print(type(index.value_counts()))
# print(index.value_counts())


# >>> index = pd.Index([3, 1, 2, 3, 4, np.nan])
# >>> index.value_counts()
# 3.0    2
# 1.0    1
# 2.0    1
# 4.0    1
# Name: count, dtype: int64

# # with open("weather-data.csv", "r") as data_file:
# #     data = data_file.readlines()
# #
# # print(data)
#
# # import csv
# #
# # with open("weather-data.csv", "r") as data_file:
# #     data = csv.reader(data_file)
# #     # print(data)
# #     temperatures = []
# #     for row in data:
# #         #print(row)
# #         if row[1] != "temp":
# #             temp_int = int(row[1])
# #             temperatures.append(temp_int)
# #             #print(temperatures)
#
# import pandas
# #https://pandas.pydata.org/
#
# # data = pandas.read_csv("weather-data.csv")
# # #print(data)
# # # print(type(data["temp"]))
# # # print(type(data))
# # data_dict = data.to_dict()
# # #print(data_dict)
# # temp_list = data["temp"].to_list()
# # # print(temp_list)
# # # print(sum(temp_list))
# # # average_temp = sum(temp_list) / len(temp_list)
# # average_temp = data["temp"].mean()
# # # print(average_temp)
# #
# # max_temp = data["temp"].max()
# # # print(max_temp)
# #
# # #Get data in columns
# # # print(data["condition"])
# # # print(data.condition)
# #
# # #Get data in rows
# # # print(data[data.day == "Monday"])
# #
# # # print(data[data.temp == data.temp.max()])
# #
# # #get Monday row
# # monday = data[data.day == "Monday"]
# # # print(monday)
# # # print("--------------")
# # # print(monday.condition)# get the condition status of Monday row
# #
# # # monday_temp = monday.temp
# # # monday_temp_F = (monday_temp*9/5)+32
# # # print(monday_temp)
# # # print(monday_temp[0])
# # # print("------")
# # # print(monday_temp_F)
#
# #create a dataframe from scratch
# data_dict = {"students": ["Amy", "James", "Angela"],
#              "scores": [76, 56, 65]}
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")
