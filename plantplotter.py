#plotting plant watering and height
import csv
import matplotlib.pyplot as plt

csv_filename = 'environmental_readings.csv'

def plantplot(filelog, param, ax=None): #func for plotting the data from the csv
    if ax is None:
        ax = plt.gca()
    ax.set_xlabel(f"Time")
    ax.set_ylabel(f"{param}")
    return ax.plot(filelog['timestamp'], filelog[param])


plantplot(csv_filename, 'Soil Moisture (%)')
plantplot(csv_filename, 'Temperature (C)')