#import libraries
import pandas as pd
import matplotlib.pyplot as plt


#open csv file
df = pd.read_csv('week04_JN_BME_output.csv')


#rename columns
df.rename(columns={
    'Timestamp': 'time',
    'Temperature (C)': 'temp',
    'Pressure (hPA)': 'pressure',
    'Humidity (%)': 'humidity'
}, inplace=True)


#convert time to datetime, set as index
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)


#find max and average temperature
max_temp_index = df['temp'].idxmax()
max_temp = df['temp'][max_temp_index]
avg_temp = df['temp'].mean()


#plot temperature
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['temp'], label='Temperature (°C)', color='blue')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.xticks(df.index[::12], df.index.strftime('%H:%M')[::12], rotation=45)
# add lines for max and average temperature
plt.axvline(x=max_temp_index, color='red', linestyle='--', label=f'Max Temp ({max_temp:.2f}°C)')
plt.axhline(y=avg_temp, color='green', linestyle='--', label=f'Average Temp ({avg_temp:.2f}°C)')
plt.title('24-Hour Temperature in Krauss Hall Office')
plt.legend()
plt.show()
plt.savefig('week06_JN_plot_temp.png', dpi=300)