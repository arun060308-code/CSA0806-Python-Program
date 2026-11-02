
import copy
import sys
import time

# 1. Represent bus stops using tuples
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar",
    (13.0674, 80.2376): "Egmore"
}

print("BUS STOP DETAILS:")

for (latitude, longitude), name in stops.items():
    print(name, ":", latitude, longitude)


# 2. Create a grid correctly using list comprehension
rows, cols = 3, 4

bad = [[0] * cols] * rows
bad[0][1] = 7

good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("\nGRID COMPARISON:")
print("Bad grid:", bad)
print("Good grid:", good)

print("Bad rows are same:", bad[0] is bad[1])
print("Good rows are same:", good[0] is good[1])


# 3. Demonstrate aliasing
original = [10, 20, 30]
alias = original

alias.append(40)

print("\nALIASING:")
print("Original:", original)
print("Alias:", alias)
print("Same object:", original is alias)


# 4. Demonstrate shallow copying
original = [[1, 2], [3, 4]]

shallow1 = copy.copy(original)
shallow2 = original[:]

shallow1[0][0] = 99

print("\nSHALLOW COPYING:")
print("Original:", original)
print("Shallow copy:", shallow1)
print("Slicing copy:", shallow2)


# 5. Demonstrate deep copying
original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)
deep[0][0] = 99

print("\nDEEP COPYING:")
print("Original:", original)
print("Deep copy:", deep)


# 6. Tuple unpacking
print("\nTUPLE UNPACKING:")

bus_stops = [
    ("Chennai Central", 13.0827, 80.2707),
    ("T. Nagar", 13.0418, 80.2341),
    ("Egmore", 13.0674, 80.2376)
]

for name, latitude, longitude in bus_stops:
    print("Stop:", name)
    print("Latitude:", latitude)
    print("Longitude:", longitude)


# 7. Compare memory of list and tuple
values_list = list(range(1000000))
values_tuple = tuple(range(1000000))

print("\nMEMORY COMPARISON:")
print("List memory:", sys.getsizeof(values_list), "bytes")
print("Tuple memory:", sys.getsizeof(values_tuple), "bytes")


# 8. Compare creation time
start = time.time()
test_list = list(range(1000000))
list_time = time.time() - start

start = time.time()
test_tuple = tuple(range(1000000))
tuple_time = time.time() - start

print("\nCREATION TIME:")
print("List creation:", round(list_time, 6), "seconds")
print("Tuple creation:", round(tuple_time, 6), "seconds")


# 9. Compare indexing time
start = time.time()

for i in range(100000):
    x = values_list[i]

list_index_time = time.time() - start

start = time.time()

for i in range(100000):
    x = values_tuple[i]

tuple_index_time = time.time() - start

print("\nINDEXING TIME:")
print("List indexing:", round(list_index_time, 6), "seconds")
print("Tuple indexing:", round(tuple_index_time, 6), "seconds")


# 10. List inside a tuple
data = ([10, 20, 30], "Bus")

data[0].append(40)

print("\nLIST INSIDE TUPLE:")
print(data)
