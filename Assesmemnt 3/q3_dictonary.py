
import random
import time
from collections import Counter

# Sample farmer complaints
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
    "water supply problem in village",
    "fertiliser not available",
    "crop damaged due to rain",
    "seeds delayed due to transport"
]

STOP = {"not", "high", "in", "due", "to", "the", "is", "a"}

# 1. Count word frequencies using dictionary get()
def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().split()

        for word in words:
            word = word.strip(".,!?")

            if word and word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts


# 2. Find top k frequent words
def top(counts, k):
    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )
    return sorted_words[:k]


# 3. Group complaints by district using setdefault()
district_complaints = [
    ("Chennai", "Seeds not received"),
    ("Madurai", "Water supply problem"),
    ("Chennai", "Fertiliser price high"),
    ("Salem", "Crop damaged due to rain"),
    ("Madurai", "Seeds delayed")
]

def group_by_district(records):
    districts = {}

    for district, complaint in records:
        districts.setdefault(district, []).append(complaint)

    return districts


# 4. Display word frequencies
word_counts = frequencies(calls, STOP)

print("WORD FREQUENCIES:")
print(word_counts)

# 5. Display top 5 frequent words
print("\nTOP 5 FREQUENT WORDS:")
print(top(word_counts, 5))

# 6. Display complaints by district
print("\nCOMPLAINTS BY DISTRICT:")

districts = group_by_district(district_complaints)

for district, complaints in districts.items():
    print(district, ":", complaints)


# 7. Experimental investigation
print("\nEXPERIMENTAL INVESTIGATION")

sizes = [1000, 10000, 100000]

for size in sizes:
    data = [random.choice(calls) for i in range(size)]

    # Dictionary method
    start = time.time()
    result = frequencies(data, STOP)
    dictionary_time = time.time() - start

    # Counter method
    start = time.time()
    counter_result = Counter(
        word.strip(".,!?")
        for text in data
        for word in text.lower().split()
        if word.strip(".,!?") and word.strip(".,!?") not in STOP
    )
    counter_time = time.time() - start

    # List count method
    start = time.time()

    all_words = [
        word.strip(".,!?")
        for text in data
        for word in text.lower().split()
        if word.strip(".,!?") and word.strip(".,!?") not in STOP
    ]

    distinct_words = set(all_words)

    list_counts = {
        word: all_words.count(word)
        for word in distinct_words
    }

    list_time = time.time() - start

    print("\nNumber of complaints:", size)
    print("Dictionary time:", round(dictionary_time, 6), "seconds")
    print("Counter time:", round(counter_time, 6), "seconds")
    print("List count time:", round(list_time, 6), "seconds")


# 8. Edge case testing
print("\nEDGE CASE TESTING")

print("Empty text:", frequencies([""], STOP))

test_calls = [
    "SEEDS delayed!",
    "Seeds received.",
    "FERTILISER price high!"
]

print("Uppercase and punctuation test:")
print(frequencies(test_calls, STOP))
