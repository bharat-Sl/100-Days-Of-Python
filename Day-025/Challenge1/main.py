#challenge 1

import os
os.chdir(r"C:\Users\bhara\Desktop\100-Days-of-Python-Projects\Day-025\Challenge1")

# import csv

# with open("weather_data.csv") as file:
#     data=csv.reader(file)
#     day=[]
#     temperatures=[]
#     condition=[]
#     for row in data:
#         if row[1]=="temp":
#             continue
#         day.append(row[0])
#         temperatures.append(int(row[1]))
#         condition.append(row[2])
#     print(temperatures)

import pandas as pd
data=pd.read_csv("weather_data.csv")
temperatures=data["temp"]
average_temp=temperatures.mean()
maximum_temp=temperatures.max()
print(f"average:{average_temp}")
print(f"maximum temperature:{maximum_temp}")

# row_maximum_temperature=data[data.temp==maximum_temp]
# print(row_maximum_temperature)

temp_monday=(int(data[data.day=="Monday"].temp)*9/5)+32
print(temp_monday)


#~~~~~~~dataframe from scratch~~~~~~~
data_dict={
    "students":["A","B","C"],
    "scores":[98,87,70]
}
data=pd.DataFrame(data_dict)
data.to_csv("new_data.csv")