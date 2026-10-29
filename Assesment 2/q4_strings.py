import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    return "".join(p + ";" for p in parts)

def build_fstring(parts):
    lines = []
    for p in parts:
        lines.append(f"{p};")
    return "".join(lines)

for n in (1000, 10000, 200000):
    sample = items[:n]

    start = time.perf_counter()
    a = build_plus(sample)
    t_plus = time.perf_counter() - start

    start = time.perf_counter()
    b = build_join(sample)
    t_join = time.perf_counter() - start

    start = time.perf_counter()
    c = build_fstring(sample)
    t_f = time.perf_counter() - start

    print("Lines:", n)
    print("Same text:", a == b == c)
    print(f"+= time: {t_plus:.4f} s")
    print(f"join time: {t_join:.4f} s")
    print(f"f-string time: {t_f:.4f} s")
    print()