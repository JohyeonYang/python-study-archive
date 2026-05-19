import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"]) # temp column values

temperature_list = data["temp"].to_list() # returning List with temp column values

average_templist = sum(temperature_list) / len(temperature_list)
print(average_templist)

print(data["temp"].mean()) # mean method

print(data["temp"].max()) # max method

print(data.temp) # as an Attribute

# Getting Data in Row
data[data.day == "Monday"]

# Getting Row data with max temp
print(data[data.temp == data.temp.max()]) #Boolean indexing

#Create a dataframe from scratch
data_dict = {
"students": ["Amy", "James", "Angela"],
"scores": [76, 56, 65]
}
data_new_dict = pandas.DataFrame(data_dict) # from dict to data frame
data_new_dict.to_csv("new_data.csv") 