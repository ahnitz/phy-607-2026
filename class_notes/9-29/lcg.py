import sys

m = 2**31
a = 1103515245
c = 12345
seed = int(sys.argv[1])

x = seed
def rand():
    global x
    x = (a * x + c) % m
    return x / m

n = 100000
v = [rand() for i in range(n)]

mean = sum(v) / n
var = sum(y * y for y in v) / n - mean**2

print(mean, 0.5)
print(var, 1 / 12)

bins = [0] * 10
for y in v:
    bins[int(y * 10)] += 1
print(bins, n / 10)

x = seed
print([rand() for i in range(3)])
x = seed
print([rand() for i in range(3)])
