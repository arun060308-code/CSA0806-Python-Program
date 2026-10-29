import sys
from functools import lru_cache

calls = 0


def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_loop(n):
    if n <= 1:
        return 1

    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


# Check answers for 1 to 6
for n in range(1, 7):
    print(n, ways_memo(n))


# Compare function calls
calls = 0
print("Naive:", ways_naive(25), "calls =", calls)

calls = 0
ways_memo.cache_clear()
print("Memo:", ways_memo(25), "calls =", calls)

print("Loop for 1000:", ways_loop(1000))
print("Recursion limit:", sys.getrecursionlimit())

try:
    print("Memo for 1000:", ways_memo(1000))
except RecursionError:
    print("RecursionError: recursion depth limit reached")