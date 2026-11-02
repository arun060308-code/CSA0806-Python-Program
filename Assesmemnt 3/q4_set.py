
# Q4 - Sets: Elective Registration Clash Detection

# 1. Store student register numbers in sets
ai_elective = {
    "192311001",
    "192311004",
    "192311007",
    "192311009"
}

iot_elective = {
    "192311002",
    "192311004",
    "192311009",
    "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}

# 2. Find students registered in both electives
both = ai_elective & iot_elective

# 3. Find students registered in exactly one elective
exactly_one = ai_elective ^ iot_elective

# 4. Find students registered in neither elective
neither = all_students - (ai_elective | iot_elective)

# 5. Display sorted results
print("ELECTIVE REGISTRATION REPORT")

print("\nAI Elective Students:")
print(sorted(ai_elective))

print("\nIoT Elective Students:")
print(sorted(iot_elective))

print("\nStudents in both electives:")
print(sorted(both))

print("\nStudents in exactly one elective:")
print(sorted(exactly_one))

print("\nStudents in neither elective:")
print(sorted(neither))

# 6. Demonstrate duplicate removal
registrations = [
    "192311001",
    "192311004",
    "192311001",
    "192311007",
    "192311004"
]

unique_students = set(registrations)

print("\nDUPLICATE REMOVAL:")
print("Original registrations:", registrations)
print("Unique registrations:", sorted(unique_students))

# 7. Demonstrate set operations
print("\nSET OPERATIONS")

print("Union:", sorted(ai_elective | iot_elective))
print("Intersection:", sorted(ai_elective & iot_elective))
print("Difference (AI - IoT):", sorted(ai_elective - iot_elective))
print("Symmetric Difference:", sorted(ai_elective ^ iot_elective))

# 8. Membership testing
print("\nMEMBERSHIP TESTING")

student = "192311004"

print("Student:", student)
print("In AI elective:", student in ai_elective)
print("In IoT elective:", student in iot_elective)

# 9. Experimental investigation
import time

print("\nEXPERIMENTAL INVESTIGATION")

sizes = [10000, 100000, 1000000]

for size in sizes:
    numbers = [str(i) for i in range(size)]
    number_set = set(numbers)

    search_value = str(size - 1)

    # List membership time
    start = time.time()

    for i in range(100):
        search_value in numbers

    list_time = time.time() - start

    # Set membership time
    start = time.time()

    for i in range(100):
        search_value in number_set

    set_time = time.time() - start

    print("\nNumber of students:", size)
    print("List search time:", round(list_time, 6), "seconds")
    print("Set search time:", round(set_time, 6), "seconds")

# 10. Test empty and identical electives
print("\nEDGE CASE TESTING")

empty_elective = set()

print("Empty elective:", empty_elective)
print("Empty intersection:", empty_elective & ai_elective)

same_elective = ai_elective.copy()

print("Identical electives intersection:",
      sorted(ai_elective & same_elective))

print("Identical electives symmetric difference:",
      sorted(ai_elective ^ same_elective))
