import time
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


# Original solution
calls = 0
start = time.perf_counter()
result1 = ways_naive(25)
time1 = time.perf_counter() - start
calls1 = calls

# Redesigned recursive solution
ways_memo.cache_clear()
calls = 0
start = time.perf_counter()
result2 = ways_memo(25)
time2 = time.perf_counter() - start
calls2 = calls

# Redesigned loop solution
start = time.perf_counter()
result3 = ways_loop(25)
time3 = time.perf_counter() - start

print("Original result:", result1)
print("Original calls:", calls1)
print(f"Original time: {time1:.6f} seconds")

print("Memoised result:", result2)
print("Memoised calls:", calls2)
print(f"Memoised time: {time2:.6f} seconds")

print("Loop result:", result3)
print(f"Loop time: {time3:.6f} seconds")

print("All results equal:", result1 == result2 == result3)