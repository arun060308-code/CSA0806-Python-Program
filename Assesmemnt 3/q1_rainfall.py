
import random
import time

# Generate rainfall readings for 365 days
readings = [round(random.uniform(0, 20), 2) for i in range(365)]

print("TOTAL DAYS:", len(readings))

# 1. Calculate weekly rainfall totals using slicing
weekly_totals = []

for i in range(0, len(readings), 7):
    week = readings[i:i+7]
    total = sum(week)
    weekly_totals.append(round(total, 2))

print("\nWEEKLY RAINFALL TOTALS:")
print(weekly_totals)

# 2. Find maximum and minimum rainfall
maximum = max(readings)
minimum = min(readings)

print("\nMAXIMUM RAINFALL:", maximum, "mm")
print("MAXIMUM DAY:", readings.index(maximum) + 1)

print("\nMINIMUM RAINFALL:", minimum, "mm")
print("MINIMUM DAY:", readings.index(minimum) + 1)

# 3. Calculate 7-day moving average
moving_average = []

for i in range(len(readings) - 6):
    average = sum(readings[i:i+7]) / 7
    moving_average.append(round(average, 2))

print("\n7-DAY MOVING AVERAGE:")
print(moving_average)

# 4. Find dry days (0 mm rainfall)
dry_days = []

for i in range(len(readings)):
    if readings[i] == 0:
        dry_days.append(i + 1)

print("\nDRY DAYS:")
print(dry_days)

# 5. Experimental investigation
print("\nEXPERIMENTAL INVESTIGATION")

sizes = [365, 36500, 365000]

for size in sizes:
    data = [random.uniform(0, 20) for i in range(size)]

    # Naive moving average
    start = time.time()

    for i in range(len(data) - 6):
        avg = sum(data[i:i+7]) / 7

    naive_time = time.time() - start

    # Running sum moving average
    start = time.time()

    if len(data) >= 7:
        total = sum(data[:7])

        for i in range(len(data) - 6):
            avg = total / 7

            if i + 7 < len(data):
                total = total - data[i] + data[i+7]

    running_time = time.time() - start

    print("\nReadings:", size)
    print("Naive time:", round(naive_time, 6), "seconds")
    print("Running sum time:", round(running_time, 6), "seconds")

# 6. Test empty and short lists
print("\nEDGE CASE TESTING")

empty_list = []
short_list = [2, 4, 6]

print("Empty list:", empty_list)
print("Short list:", short_list)

if len(empty_list) < 7:
    print("Empty list: Not enough readings for moving average")

if len(short_list) < 7:
    print("Short list: Not enough readings for moving average")
