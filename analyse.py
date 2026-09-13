import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Weather :
    def __init__(self,name,date,data):
        self.name = name 
        self.date = date
        self.data = data
       
    def operation(self):
        min_time = self.date[np.argmin(self.data)]
        max_time = self.date[np.argmax(self.data)]
        print(f"\n{self.name}")
        print(f"Average : {np.mean(self.data):.2f} ")
        print(f"Minimum: {np.min(self.data)} -> {min_time}")
        print(f"Maximum : {np.max(self.data)} -> {max_time} ")

#Extract data from csv file
berlin = pd.read_csv("berlin_weather_2025.csv")
date = np.array(berlin["date"])
min_temperature = np.array(berlin["temperature_min"])
max_temperature = np.array(berlin["temperature_max"])
rainfall = np.array(berlin["rainfall"])
wind_speed = np.array(berlin["wind_speed"])

#Giving values
min_temp = Weather("Minimum Temperature",date,min_temperature)
max_temp = Weather("Maximum Temperature",date,max_temperature)
rain = Weather("Rainfall",date,rainfall)
wind = Weather("Wind Speed",date,wind_speed)

#Final output
print("\n============= Weather Analysis =============")
min_temp.operation()
max_temp.operation()
rain.operation()
wind.operation()

# Covert date to months
berlin["date"] = pd.to_datetime(berlin["date"])

monthly_min_temp = berlin.groupby(berlin["date"].dt.month)["temperature_min"].mean()

monthly_max_temp = berlin.groupby(berlin["date"].dt.month)["temperature_max"].mean()

monthly_rainfall = berlin.groupby(berlin["date"].dt.month)["rainfall"].sum()

monthly_wind_speed = berlin.groupby(berlin["date"].dt.month)["wind_speed"].mean()

month = monthly_min_temp.index

#Graph
plt.figure(figsize=(12, 8))

# Minimum Temperature
plt.subplot(2, 2, 1)
plt.plot(month, monthly_min_temp.values, marker="o")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Average Minimum Temperature")
plt.xticks(range(1, 13))
plt.grid(True)

# Maximum Temperature
plt.subplot(2, 2, 2)
plt.plot(month, monthly_max_temp.values, marker="o")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Average Maximum Temperature")
plt.xticks(range(1, 13))
plt.grid(True)

# Rainfall
plt.subplot(2, 2, 3)
plt.bar(month, monthly_rainfall.values)
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Total Rainfall")
plt.xticks(range(1, 13))
plt.grid(True)

# Wind Speed
plt.subplot(2, 2, 4)
plt.plot(month, monthly_wind_speed.values, marker="o")
plt.xlabel("Month")
plt.ylabel("Wind Speed (km/h)")
plt.title("Monthly Average Wind Speed")
plt.xticks(range(1, 13))
plt.grid(True)

plt.tight_layout()
plt.show()