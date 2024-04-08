from datetime import datetime
import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))  


fig, ax = plt.subplots(dpi=128, figsize=(10, 6))


ax.plot(dates, highs, c='red')


ax.set_title("Daily high temperatures, July 2014", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)


plt.show()
