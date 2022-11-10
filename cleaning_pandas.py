# %%
print('Data cleaning with pandas')

#library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Import data
flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()

#Pandas Data Filtering/Sorting Question Answering
#Question 1 How many flights were there from JFK to SLC? Int
num_one = flights_data[(flights_data['origin'] == 'JFK') & (flights_data['dest'] == 'SLC')]
print(len(num_one))

#Question 2 How many airlines fly to SLC? Should be int
num_two = flights_data[flights_data['dest'] == 'SLC']
print(len(num_two))

#Question 3 What is the average arrival delay for flights to RDU? float
num_three = flights_data.where(flights_data['dest'] == 'RDU')['arr_delay'].mean()
print(num_three)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
#Find the flights to SEA
flights_to_SEA = flights_data[flights_data['dest'] == 'SEA']
#Find the number of flights from NYC airports
#Flights from LGA
flights_from_LGA = flights_to_SEA[flights_to_SEA['origin'] == 'LGA']
#Flights from JFK
flights_from_JFK = flights_to_SEA[flights_to_SEA['origin'] == 'JFK']
#flights from NYC
flights_from_NYC = flights_from_LGA.append(flights_from_JFK)
num_four = len(flights_from_NYC) / len(flights_to_SEA)
print(num_four)

#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
#delay by date
#slice data delay by date
delay_by_date = flights_data[['year', 'month', 'day', 'dep_delay']]
#finding the average delay
dep_delay_date = (delay_by_date.copy().assign(date = lambda row: pd.to_datetime(row [['year', 'month', 'day']])).groupby('date').mean())
#finding the largest delay
num_five = dep_delay_date.nlargest(1, 'dep_delay')
print(num_five)

#Question 6 Which date has the largest average arrival delay? pd slice with date and float
#slice date delay by date
delay_by_date2 = flights_data [['year', 'month', 'day', 'arr_delay']]
#find the average delay
arr_delay_date = (delay_by_date2.copy().assign(date = lambda row: pd.to_datetime(row [['year', 'month', 'day']])).groupby('date').mean())
#find the largest delay
num_six = arr_delay_date.nlargest(1, 'arr_delay')
print(num_six)

#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
fly_data = flights_data[['tailnum', 'flight','origin', 'air_time', 'distance']]
#find LGA flights
LGA_flights = fly_data [fly_data['origin'] == 'LGA']
#find JFK flights
JFK_flights = fly_data [fly_data['origin'] == 'JFK']
#combine flight lists
LGA_JFK_flights = LGA_flights.append(JFK_flights)
#find speed
LGA_JFK_flights ['speed'] = (LGA_JFK_flights ['distance'] / LGA_JFK_flights ['air_time'])
num_seven = LGA_JFK_flights.nlargest(1, 'speed')
print(num_seven)

#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
print(weather_data_pd)
num_eight = weather_data_pd.fillna(value = 0)
print(num_eight)

#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
weather_data_months = weather_data_np[:, 3]
feb_weather = weather_data_months == 2
num_nine = weather_data_np[feb_weather]
print(len(num_nine))

#Question 10 What was the mean for humidity in February? Float
feb_humidity = num_nine[:, 8]
print(feb_humidity)
num_ten = feb_humidity.mean()
print(num_ten)

#Question 11 What was the std for humidity in February? Float
num_eleven = feb_humidity.std()
print(num_eleven)


