
import time
import sys
import random

# ---------------------------------
# 1. Create train timetable
# ---------------------------------

trains = {
    101: {
        "name": "Chennai Express",
        "stops": [
            ("Chennai Central", "06:00", "06:10"),
            ("Arakkonam", "07:00", "07:05"),
            ("Katpadi", "08:00", "08:05")
        ],
        "running_days": {"Monday", "Wednesday", "Friday"}
    },

    102: {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai Central", "07:00", "07:15"),
            ("Salem", "10:00", "10:05"),
            ("Coimbatore", "12:00", "12:10")
        ],
        "running_days": {"Monday", "Tuesday", "Thursday"}
    },

    103: {
        "name": "Bangalore Mail",
        "stops": [
            ("Chennai Central", "08:00", "08:10"),
            ("Katpadi", "10:00", "10:05"),
            ("Bangalore", "13:00", "13:10")
        ],
        "running_days": {"Tuesday", "Thursday", "Saturday"}
    },

    104: {
        "name": "Mysore Express",
        "stops": [
            ("Chennai Central", "09:00", "09:10"),
            ("Arakkonam", "10:00", "10:05"),
            ("Mysore", "14:00", "14:10")
        ],
        "running_days": {"Monday", "Friday", "Sunday"}
    },

    105: {
        "name": "Kerala Express",
        "stops": [
            ("Chennai Central", "10:00", "10:10"),
            ("Salem", "12:00", "12:05"),
            ("Ernakulam", "16:00", "16:10")
        ],
        "running_days": {"Wednesday", "Friday", "Sunday"}
    }
}

# ---------------------------------
# 2. Search without index
# ---------------------------------

def search_without_index(data, station, day):
    results = []

    for train_no, details in data.items():
        if day in details["running_days"]:
            for stop in details["stops"]:
                if stop[0] == station:
                    results.append(
                        (train_no, details["name"], stop[2])
                    )

    return sorted(results, key=lambda x: x[2])


# ---------------------------------
# 3. Create station index
# ---------------------------------

def create_station_index(data):
    index = {}

    for train_no, details in data.items():
        for stop in details["stops"]:
            station = stop[0]

            if station not in index:
                index[station] = []

            index[station].append(train_no)

    return index


# ---------------------------------
# 4. Search using index
# ---------------------------------

def search_with_index(data, index, station, day):
    results = []

    for train_no in index.get(station, []):
        details = data[train_no]

        if day in details["running_days"]:
            for stop in details["stops"]:
                if stop[0] == station:
                    results.append(
                        (train_no, details["name"], stop[2])
                    )

    return sorted(results, key=lambda x: x[2])


# ---------------------------------
# 5. Display timetable
# ---------------------------------

print("TRAIN TIMETABLE")
print("-" * 60)

for train_no, details in trains.items():
    print("\nTrain Number:", train_no)
    print("Train Name:", details["name"])
    print("Running Days:", sorted(details["running_days"]))

    for station, arrival, departure in details["stops"]:
        print(station, "| Arrival:", arrival,
              "| Departure:", departure)


# ---------------------------------
# 6. Search train by station and day
# ---------------------------------

station = "Chennai Central"
day = "Monday"

print("\nTRAINS STOPPING AT", station)
print("Day:", day)
print("-" * 60)

station_index = create_station_index(trains)

results = search_with_index(
    trains, station_index, station, day
)

if results:
    for train_no, name, departure in results:
        print(train_no, name, "| Departure:", departure)
else:
    print("No trains found.")


# ---------------------------------
# 7. Test unknown station and day
# ---------------------------------

print("\nUNKNOWN STATION TEST")

unknown = search_with_index(
    trains, station_index, "Unknown Station", "Monday"
)

print("Result:", unknown)

print("\nNON-RUNNING DAY TEST")

not_running = search_with_index(
    trains, station_index, "Chennai Central", "Tuesday"
)

print("Result:", not_running)


# ---------------------------------
# 8. Generate timetable for testing
# ---------------------------------

stations = [
    "Chennai Central",
    "Arakkonam",
    "Katpadi",
    "Salem",
    "Bangalore"
]

days = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]


def generate_timetable(number):
    data = {}

    for i in range(number):
        train_no = 1000 + i
        selected_stations = random.sample(stations, 3)

        stops = []

        for j, station_name in enumerate(selected_stations):
            arrival_hour = 6 + j
            arrival = f"{arrival_hour:02d}:00"
            departure = f"{arrival_hour:02d}:10"

            stops.append(
                (station_name, arrival, departure)
            )

        data[train_no] = {
            "name": "Train " + str(train_no),
            "stops": stops,
            "running_days": set(random.sample(days, 3))
        }

    return data


# ---------------------------------
# 9. Performance comparison
# ---------------------------------

print("\nPERFORMANCE COMPARISON")
print("-" * 60)

for size in [100, 1000, 10000]:

    test_data = generate_timetable(size)
    test_station = "Chennai Central"
    test_day = "Monday"

    start = time.perf_counter()

    search_without_index(
        test_data, test_station, test_day
    )

    without_time = time.perf_counter() - start

    start = time.perf_counter()

    test_index = create_station_index(test_data)

    search_with_index(
        test_data, test_index, test_station, test_day
    )

    with_time = time.perf_counter() - start

    print("\nNumber of trains:", size)
    print("Without index:", without_time)
    print("With index (including index creation):", with_time)


# ---------------------------------
# 10. Estimate index memory
# ---------------------------------

index_memory = sys.getsizeof(station_index)

for key, value in station_index.items():
    index_memory += sys.getsizeof(key)
    index_memory += sys.getsizeof(value)

    for train_no in value:
        index_memory += sys.getsizeof(train_no)

print("\nSTATION INDEX MEMORY")
print("Approximate memory:", index_memory, "bytes")
