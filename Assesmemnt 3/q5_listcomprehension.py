
import random
import time
import sys

# 1. Sample temperature readings in Celsius
readings = [2, 5, 55, -60, 8, 10, 4, 52, -5, 7]

print("ORIGINAL TEMPERATURE READINGS:")
print(readings)

# 2. Clean readings using for loop and append()
valid_readings = []

for temp in readings:
    if -50 <= temp <= 50:
        valid_readings.append(temp)

print("\nVALID READINGS USING FOR LOOP:")
print(valid_readings)

# 3. Convert Celsius to Fahrenheit using for loop
fahrenheit = []

for temp in valid_readings:
    f = (temp * 9/5) + 32
    fahrenheit.append(round(f, 2))

print("\nTEMPERATURE IN FAHRENHEIT:")
print(fahrenheit)

# 4. Clean readings using list comprehension
cleaned = [temp for temp in readings if -50 <= temp <= 50]

print("\nVALID READINGS USING LIST COMPREHENSION:")
print(cleaned)

# 5. Convert Celsius to Fahrenheit using list comprehension
fahrenheit_comp = [
    round((temp * 9/5) + 32, 2)
    for temp in cleaned
]

print("\nFAHRENHEIT USING LIST COMPREHENSION:")
print(fahrenheit_comp)

# 6. Use map() and filter() with lambda
filtered = list(filter(lambda temp: -50 <= temp <= 50, readings))

converted = list(map(lambda temp: round((temp * 9/5) + 32, 2), filtered))

print("\nVALID READINGS USING FILTER:")
print(filtered)

print("\nFAHRENHEIT USING MAP:")
print(converted)

# 7. Find alarm minutes using enumerate()
alarm_minutes = []

for minute, temp in enumerate(readings, start=1):
    if temp < 2 or temp > 8:
        alarm_minutes.append(minute)

print("\nALARM MINUTES:")
print(alarm_minutes)

# 8. Dictionary comprehension
temperature_dict = {
    minute: temp
    for minute, temp in enumerate(readings, start=1)
    if -50 <= temp <= 50
}

print("\nVALID TEMPERATURE DICTIONARY:")
print(temperature_dict)

# 9. Set comprehension
temperature_set = {
    temp for temp in readings if -50 <= temp <= 50
}

print("\nUNIQUE VALID TEMPERATURES:")
print(sorted(temperature_set))

# 10. Experimental investigation
print("\nEXPERIMENTAL INVESTIGATION")

sizes = [10000, 100000, 1000000]

for size in sizes:

    data = [random.uniform(-60, 60) for i in range(size)]

    # For loop method
    start = time.time()

    result1 = []
    for temp in data:
        if -50 <= temp <= 50:
            result1.append(temp)

    loop_time = time.time() - start

    # List comprehension method
    start = time.time()

    result2 = [temp for temp in data if -50 <= temp <= 50]

    comprehension_time = time.time() - start

    # Filter method
    start = time.time()

    result3 = list(filter(lambda temp: -50 <= temp <= 50, data))

    filter_time = time.time() - start

    print("\nNumber of readings:", size)
    print("For loop time:", round(loop_time, 6), "seconds")
    print("List comprehension time:", round(comprehension_time, 6), "seconds")
    print("Filter time:", round(filter_time, 6), "seconds")

    print("All results identical:", result1 == result2 == result3)

# 11. Memory comparison
sample_data = [i for i in range(10000)]

list_result = [x for x in sample_data if x % 2 == 0]

generator_result = (x for x in sample_data if x % 2 == 0)

print("\nMEMORY COMPARISON:")
print("List memory:", sys.getsizeof(list_result), "bytes")
print("Generator memory:", sys.getsizeof(generator_result), "bytes")

# 12. Edge case testing
print("\nEDGE CASE TESTING")

all_valid = [2, 3, 4, 5, 6, 7, 8]
all_invalid = [55, 60, -55, -70]

print("All valid readings:", [x for x in all_valid if -50 <= x <= 50])
print("All invalid readings:", [x for x in all_invalid if -50 <= x <= 50])
