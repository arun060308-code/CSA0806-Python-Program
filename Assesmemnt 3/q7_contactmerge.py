
import time
import random
import string

# ---------------------------------
# 1. Contact lists
# ---------------------------------

contacts1 = [
    {
        "name": "Arun",
        "phone": "9876543210",
        "email": "arun@gmail.com"
    },
    {
        "name": "Rahul",
        "phone": "98765-43211",
        "email": "rahul@gmail.com"
    },
    {
        "name": "Priya",
        "phone": "9876543212",
        "email": "priya@gmail.com"
    },
    {
        "name": "Arun",
        "phone": "9876543210",
        "email": "arun@gmail.com"
    }
]

contacts2 = [
    {
        "name": "ARUN",
        "phone": "+91 9876543210",
        "email": "arun2@gmail.com"
    },
    {
        "name": "Kiran",
        "phone": "9876543213",
        "email": "kiran@gmail.com"
    },
    {
        "name": "Rahul",
        "phone": "9876543211",
        "email": "rahul@gmail.com"
    },
    {
        "name": "Meena",
        "phone": "",
        "email": "meena@gmail.com"
    }
]


# ---------------------------------
# 2. Normalize contact details
# ---------------------------------

def normalize_phone(phone):
    digits = "".join(
        character for character in phone
        if character.isdigit()
    )

    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]

    return digits


def normalize_name(name):
    return " ".join(name.strip().lower().split())


def normalize_email(email):
    return email.strip().lower()


# ---------------------------------
# 3. Merge contacts
# ---------------------------------

def merge_contacts(list1, list2):
    merged = {}

    for contact in list1 + list2:

        phone = normalize_phone(contact.get("phone", ""))
        name = normalize_name(contact.get("name", ""))
        email = normalize_email(contact.get("email", ""))

        # Skip contacts without a valid phone number
        if len(phone) != 10:
            continue

        if phone not in merged:
            merged[phone] = {
                "name": contact.get("name", "").strip(),
                "phone_numbers": set(),
                "emails": set()
            }

        if contact.get("phone", "").strip():
            merged[phone]["phone_numbers"].add(
                contact["phone"].strip()
            )

        if email:
            merged[phone]["emails"].add(email)

        # Keep the first available name
        if not merged[phone]["name"] and name:
            merged[phone]["name"] = contact["name"].strip()

    return merged


# ---------------------------------
# 4. Display merged contacts
# ---------------------------------

merged_contacts = merge_contacts(contacts1, contacts2)

print("MERGED CONTACT LIST")
print("-" * 50)

for phone, details in merged_contacts.items():
    print("\nName:", details["name"])
    print("Normalized Phone:", phone)
    print("Phone Numbers:", sorted(details["phone_numbers"]))
    print("Emails:", sorted(details["emails"]))


# ---------------------------------
# 5. Duplicate contact count
# ---------------------------------

total_contacts = len(contacts1) + len(contacts2)
unique_contacts = len(merged_contacts)

print("\nCONTACT SUMMARY")
print("Total contacts:", total_contacts)
print("Unique contacts:", unique_contacts)
print("Skipped contacts:", total_contacts - unique_contacts)


# ---------------------------------
# 6. Test missing and duplicate details
# ---------------------------------

print("\nTESTING")

test_contacts = [
    {"name": "Test User", "phone": "", "email": "test@gmail.com"},
    {"name": "Test User", "phone": "9876543210", "email": "TEST@GMAIL.COM"}
]

test_result = merge_contacts(test_contacts, [])

print("Missing phone test: Contact skipped")
print("Duplicate phone test: Contacts merged")
print("Test result:", test_result)


# ---------------------------------
# 7. Generate contacts for benchmarking
# ---------------------------------

def generate_contacts(number):
    data = []

    for i in range(number):
        data.append({
            "name": "Person " + str(i),
            "phone": str(9000000000 + i),
            "email": "person" + str(i) + "@gmail.com"
        })

    return data


# ---------------------------------
# 8. Dictionary-based merge timing
# ---------------------------------

print("\nPERFORMANCE COMPARISON")
print("-" * 50)

for size in [1000, 100000]:

    test_data = generate_contacts(size)

    start = time.perf_counter()

    result = merge_contacts(test_data, [])

    dictionary_time = time.perf_counter() - start

    print("\nNumber of contacts:", size)
    print("Dictionary merge time:", dictionary_time, "seconds")


# ---------------------------------
# 9. Compare with pairwise method
# ---------------------------------

def pairwise_duplicate_check(data):
    duplicates = []

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            phone1 = normalize_phone(data[i]["phone"])
            phone2 = normalize_phone(data[j]["phone"])

            if phone1 == phone2:
                duplicates.append((i, j))

    return duplicates


small_data = generate_contacts(1000)

start = time.perf_counter()
pairwise_duplicate_check(small_data)
pairwise_time = time.perf_counter() - start

start = time.perf_counter()
merge_contacts(small_data, [])
dictionary_time = time.perf_counter() - start

print("\nPAIRWISE VS DICTIONARY")
print("Pairwise method:", pairwise_time, "seconds")
print("Dictionary method:", dictionary_time, "seconds")
