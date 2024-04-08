from datetime import datetime
import csv
import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


fig, ax = plt.subplots(dpi=128, figsize=(10, 6))
ax.plot(dates, highs, c='red', alpha=0.5, label='Highs')
ax.plot(dates, lows, c='blue', alpha=0.5, label='Lows')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


ax.set_title("Daily high and low temperatures, July 2014", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.legend()

plt.show()
