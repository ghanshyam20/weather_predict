# with open("weather_data.csv") as data_file:
#             data=data_file.readlines()
#             print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)

#     temperatures=[]

#     for row in  data:
#         if row[1] !="temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

#this is ther good approach 
import pandas


data=pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data))

data_dict =data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()

print(temp_list)


print(data["temp"].mean()) #this is the correctd method to do

#get data in columns 

print(data["condition"])

print(data[data.day=="Monday"])



print(data[data.temp==data.temp.max()])

