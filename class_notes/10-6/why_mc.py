import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(1)
targets = (10**3, 10**4, 10**5, 10**6)


def f(x):
    return (x**2).sum(axis=-1)

def grid(d, n):
    g = (np.arange(n) + 0.5) / n
    p = np.stack(np.meshgrid(*([g] * d), indexing="ij"), -1).reshape(-1, d)
    return abs(f(p).mean() - d / 3)

def mc(d, N):
    e = [f(rng.random((N, d))).mean() - d / 3 for _ in range(10)]
    return np.sqrt(np.mean(np.square(e)))

for d in [2, 8]:
    ns = [max(2, round(t ** (1 / d))) for t in targets]
    Ns = [n**d for n in ns]
    plt.loglog(Ns, [grid(d, n) for n in ns], "o-", color='red', label=f"grid, d={d}")
    plt.loglog(Ns, [mc(d, N) for N in Ns], "s--", color='green', label=f"mc, d={d}")

plt.xlabel("N")
plt.ylabel("error")
plt.legend()
plt.savefig("why_mc.png", dpi=140)
plt.show()
