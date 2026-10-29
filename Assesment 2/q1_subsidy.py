def subsidy_separate(units, ration_card, elderly):
    if units <= 100:
        print("Full subsidy")

    if 101 <= units <= 200 and ration_card:
        print("Partial subsidy")

    if units > 200 and elderly:
        print("Special subsidy")

    if (101 <= units <= 200 and not ration_card) or (units > 200 and not elderly):
        print("No subsidy")


def subsidy_chained(units, ration_card, elderly):
    if units <= 100:
        print("Full subsidy")
    elif 101 <= units <= 200:
        if ration_card:
            print("Partial subsidy")
        else:
            print("No subsidy")
    elif units > 200:
        if elderly:
            print("Special subsidy")
        else:
            print("No subsidy")


households = [
    (100, False, False),
    (101, True, False),
    (101, False, False),
    (200, True, False),
    (200, False, False),
    (201, False, True),
    (201, False, False),
    (80, True, True)
]

print("=== Separate if statements ===")
for units, ration, elderly in households:
    print(units, ration, elderly, end=" -> ")
    subsidy_separate(units, ration, elderly)

print("\n=== if-elif-else ===")
for units, ration, elderly in households:
    print(units, ration, elderly, end=" -> ")
    subsidy_chained(units, ration, elderly)