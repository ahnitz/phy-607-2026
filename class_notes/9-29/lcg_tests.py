import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

A, C, M = 1103515245, 12345, 2**31


def lcg_int(n, a=A, c=C, m=M, seed=1):
    x = seed
    out = np.empty(n, dtype=np.int64)
    for i in range(n):
        x = (a * x + c) % m
        out[i] = x
    return out


def period(a=A, c=C, m=M, seed=1):
    x = (a * seed + c) % m
    n = 1
    while x != seed:
        x = (a * x + c) % m
        n += 1
    return n


def bit_period(bits, limit=4096):
    for p in range(1, limit):
        if np.array_equal(bits[:2000], bits[p:2000 + p]):
            return p
    return None


n = 200000
ints = lcg_int(n)
v = ints / M

print("WHAT IT PASSES")
print(f"  mean            {v.mean():.6f}   expect 0.5")
print(f"  variance        {v.var():.6f}   expect {1 / 12:.6f}")
for k in (1, 2, 5, 10):
    print(f"  autocorr lag {k:2d}  {np.corrcoef(v[:-k], v[k:])[0, 1]:+.5f}"
          f"     expect 0 +/- {1 / np.sqrt(n):.5f}")

print("\nWHAT IT FAILS")
print("  bit 0 is the last binary digit of each number")
for j in range(6):
    print(f"  bit {j} repeats every {bit_period((ints >> j) & 1):4d} values"
          f"      (2^{j + 1} = {2**(j + 1)})")

print("\nAND IT DOES REPEAT")
for m in (2**8, 2**10, 2**12, 2**16, 2**20):
    print(f"  m = {m:9d}   full sequence repeats after {period(m=m):9d}")

fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(15, 4.6))

exp = n / 50
a1.hist(v, bins=50, color="#2980b9")
a1.axhline(exp, color="#c0392b", lw=1.5)
for s in (-3, 3):
    a1.axhline(exp + s * np.sqrt(exp), color="#c0392b", ls=":", lw=1)
a1.set_title("passes: the histogram is flat\n"
             "red = expected, dotted = 3 sigma")
a1.set_xlabel("value")
a1.set_ylabel("count")

b = (ints >> 0) & 1
a2.step(range(40), b[:40], where="mid", color="#c0392b")
a2.plot(range(40), b[:40], "o", ms=4, color="#c0392b")
a2.set_ylim(-0.3, 1.3)
a2.set_yticks([0, 1])
a2.set_title("fails: the last bit just alternates\n"
             "0,1,0,1 forever - period 2")
a2.set_xlabel("i")
a2.set_ylabel("low bit of $x_i$")

s = lcg_int(256, m=256) / 256
a3.plot(s[:-1], s[1:], ".", ms=5, color="#c0392b")
a3.set_title("fails: consecutive pairs lie on a lattice\n"
             "(shown for m = 256, true at every m)")
a3.set_xlabel("$x_i$")
a3.set_ylabel("$x_{i+1}$")
a3.set_aspect("equal")

fig.suptitle("A linear congruential generator: passing the easy tests is not "
             "the same as being random", weight="bold")
fig.tight_layout()
fig.savefig("lcg_tests.png", dpi=140)
print("\nwrote lcg_tests.png")
