import numpy as np
import matplotlib.pyplot as plt

months = np.array(["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"])

temp = np.array([21,29,31,38,41,39,34,35,37,27,21,20])

rain = np.array([8,5,7,3,12,7,8,4,7,2,5,10])

humidity = np.array([12,13,26,18,24,32,14,36,17,33,12,32])

wind_speed = np.array([12,13,15,12,16,17,13,15,16,13,19,14])

average_temp = np.mean(temp)
high_temp = np.max(temp)
low_temp = np.min(temp)

average_rain = np.mean(rain)
high_rain = np.max(rain)
low_rain = np.min(rain)

average_humi = np.mean(humidity)
high_humi = np.max(humidity)
low_humi = np.min(humidity)

average_wind = np.mean(wind_speed)
high_wind = np.max(wind_speed)
low_wind = np.min(wind_speed)

temp_hotest_index = np.argmax(temp)
temp_hotest_month = months[temp_hotest_index]

temp_coolest_index = np.argmin(temp)
temp_coolest_month = months[temp_coolest_index]

rain_highest_index = np.argmax(rain)
rain_higest_month = months[rain_highest_index]

rain_lowest_index = np.argmin(rain)
rain_lowest_month = months[rain_lowest_index]

humi_highest_index = np.argmax(humidity)
humidity_highest_month = months[humi_highest_index]

humi_lowest_index = np.argmin(humidity)
humidity_lowest_month = months[humi_lowest_index]

wind_highest_index = np.argmax(wind_speed)
wind_highest_month = months[wind_highest_index]

wind_lowest_index = np.argmin(wind_speed)
wind_lowest_month = months[wind_highest_index]

print("============ Weather Data ============")

print("\nTemperature")
print(f"Average       : {average_temp:.2f} °C")
print(f"Highest       : {high_temp:.2f} °C")
print(f"Lowest        : {low_temp:.2f} °C")
print(f"Hottest Month : {temp_hotest_month}")
print(f"Coldest Month : {temp_coolest_month}")

print("\nRainfall")
print(f"Average       : {average_rain:.2f} times")
print(f"Highest       : {high_rain} times")
print(f"Lowest        : {low_rain} times")
print(f"Higest Rainfall : {rain_higest_month}")
print(f"Lowest Rainfall : {rain_lowest_month}")

print("\nHumidity")
print(f"Average       : {average_humi:.2f} %")
print(f"Highest       : {high_humi:.2f} %")
print(f"Lowest        : {low_humi:.2f} %")
print(f"Highest Month : {humidity_highest_month}")
print(f"Lowest Month  : {humidity_lowest_month}")

print("\nWind Speed")
print(f"Average       : {average_wind:.2f}")
print(f"Highest       : {high_wind:.2f}")
print(f"Lowest        : {low_wind:.2f}")
print(f"Highest Month : {wind_highest_month}")
print(f"Lowest Month  : {wind_lowest_month}")

print("=" * 40)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.bar(months, temp)
plt.xlabel("Months")
plt.ylabel("Temperature °C")
plt.title("Temperature")

plt.subplot(2, 2, 2)
plt.bar(months, rain)
plt.xlabel("Months")
plt.ylabel("How many times rainfall")
plt.title("Rainfall")

plt.subplot(2, 2, 3)
plt.bar(months, humidity)
plt.xlabel("Months")
plt.ylabel("Humidity")
plt.title("Humidity")

plt.subplot(2, 2, 4)
plt.bar(months, wind_speed)
plt.xlabel("Months")
plt.ylabel("Wind speed")
plt.title("Wind speed")

plt.tight_layout()
plt.show()