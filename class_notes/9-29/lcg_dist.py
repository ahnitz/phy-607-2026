import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

a, c, m = 1103515245, 12345, 2**31


def rand(n, seed=1):
    x = seed
    out = np.empty(n)
    for i in range(n):
        x = (a * x + c) % m
        out[i] = x / m
    return out


n = 200000
u = rand(2 * n)
u1, u2 = u[:n], u[n:]

expo = -np.log(1 - u1)
gauss = np.sqrt(-2 * np.log(1 - u1)) * np.cos(2 * np.pi * u2)

print(f"uniform      mean {u1.mean():+.4f} expect  0.5000"
      f"   std {u1.std():.4f} expect {np.sqrt(1 / 12):.4f}")
print(f"exponential  mean {expo.mean():+.4f} expect  1.0000"
      f"   std {expo.std():.4f} expect 1.0000")
print(f"gaussian     mean {gauss.mean():+.4f} expect  0.0000"
      f"   std {gauss.std():.4f} expect 1.0000")

fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(14.5, 4.3))

a1.hist(u1, bins=60, density=True, color="#2980b9")
t = np.linspace(0, 1, 200)
a1.plot(t, np.ones_like(t), color="#c0392b", lw=2)
a1.set_title("uniform, straight from the generator\n$p(u) = 1$")

a2.hist(expo, bins=60, range=(0, 8), density=True, color="#2980b9")
t = np.linspace(0, 8, 200)
a2.plot(t, np.exp(-t), color="#c0392b", lw=2)
a2.set_title("exponential, by inverse CDF\n$x=-\\ln(1-u)$,   $p(x)=e^{-x}$")

a3.hist(gauss, bins=60, range=(-4, 4), density=True, color="#2980b9")
t = np.linspace(-4, 4, 200)
a3.plot(t, np.exp(-t**2 / 2) / np.sqrt(2 * np.pi), color="#c0392b", lw=2)
a3.set_title("gaussian, by Box-Muller\n$z=\\sqrt{-2\\ln(1-u_1)}\\cos(2\\pi u_2)$")

for ax in (a1, a2, a3):
    ax.set_ylabel("density")
    ax.grid(alpha=0.25)

fig.suptitle("One uniform generator, any distribution you want "
             "(red = the pdf we are aiming for)", weight="bold")
fig.tight_layout()
fig.savefig("lcg_dist.png", dpi=140)
print("\nwrote lcg_dist.png")
