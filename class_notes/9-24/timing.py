import timeit

for n in [1000, 10000, 100000, 1000000]:
    setup = f"data = list(range({n})); s = set(data)"
    t1 = timeit.timeit(f"{n - 1} in data", setup, number=100)
    t2 = timeit.timeit(f"{n - 1} in s", setup, number=100)
    print(n, t1, t2, t1 / t2)
