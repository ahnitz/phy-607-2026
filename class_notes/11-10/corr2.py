import numpy as np

def generate_sticky_chain(n_samples, mix_frac):
    """
    Generates a chain that only 'mixes' (updates) a fraction of the time.
    Theory ACL = (2 / mix_frac) - 1
    """
    chain = np.zeros(n_samples)
    chain[0] = np.random.randn()
    
    # Pre-generate all possible new samples (pure noise)
    proposals = np.random.randn(n_samples)
    # Pre-generate decision to mix or stick
    # True = mix (update), False = stick (repeat)
    do_mix = np.random.rand(n_samples) < mix_frac
    
    for i in range(1, n_samples):
        if do_mix[i]:
            chain[i] = proposals[i]
        else:
            chain[i] = chain[i-1]
            
    return chain

def simple_autocorr(chain):
    """
    Simple direct ACL estimator (summing rho until it goes negative).
    """
    y = chain - np.mean(chain)
    # Compute full autocorrelation
    rho = np.correlate(y, y, mode='full')
    rho = rho[len(rho)//2:] # Keep positive lags
    rho = rho / rho[0]      # Normalize
    
    # Sum until standard deviation of noise makes it negative
    cutoff = np.where(rho < 0)[0]
    cutoff = cutoff[0] if len(cutoff) > 0 else len(rho)
    
    return 1.0 + 2.0 * np.sum(rho[1:cutoff])

# =============================
# Demo
# =============================
N = 100000
MIX_FRAC = 0.1  # Mix only 10% of the time
THEORY = (2 / MIX_FRAC) - 1

print(f"Generating Sticky Chain with mixing fraction: {MIX_FRAC}")
print(f"Theoretical ACL: {THEORY:.1f}")

chain = generate_sticky_chain(N, MIX_FRAC)
calculated_acl = simple_autocorr(chain)

print(f"Calculated ACL:  {calculated_acl:.2f}")

# Sanity check: The chain should look 'blocky' compared to AR(1)
# showing it getting stuck at specific values.
import matplotlib.pyplot as plt
plt.figure(figsize=(10,3))
plt.plot(chain[:500], marker='.', linestyle='-', alpha=0.6)
plt.title("First 500 steps of Sticky Chain (Notice the flat 'stuck' periods)")
plt.xlabel("Step")
plt.show()
