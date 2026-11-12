import numpy as np
import arviz as az
from scipy.stats import ks_2samp

# The same range used for the tests. 
# Try raising the burn in and test end point to see where the chaing
# converges
burn_in = 0
end = 200

rng = np.random.default_rng(0)

def demo(nwalkers=60, nsteps=4000, width=0.5, x0=40.0):
    # log space, so walkers can start far out at x0 and have a real burn-in
    lp = lambda x: -0.5 * x**2 + 2 * np.log(abs(np.sin(2 * x)) + 1e-300)
    out = np.empty((nwalkers, nsteps, 1))
    for w in range(nwalkers):
        x, l = x0, lp(x0)
        for i in range(nsteps):
            xt = x + rng.normal(0, width)
            lt = lp(xt)
            if np.log(rng.random()) < lt - l:
                x, l = xt, lt
            out[w, i, 0] = x
    return out


chain = demo(nsteps=end)
par = chain[:, burn_in:end, 0]   # shape (chain, draw), one parameter
nw, ns = par.shape
print("testing steps", burn_in, "to", end, "of", chain.shape[1])

# 1. gelman-rubin, compares variance between chains to variance within them
# https://python.arviz.org/en/stable/api/generated/arviz.rhat.html
print("r_hat                ", az.rhat(par))

# 2. autocorrelation length and the number of samples you actually have
# https://emcee.readthedocs.io/en/stable/tutorials/autocorr/
ess = az.ess(par)
# r_hat cannot be resolved below about 1 + 1/(draws per walker), so read it
# next to that number rather than against a fixed threshold
print("ess                  ", round(ess), " acl ~", round(nw * ns / ess, 1),
      " effective draws per walker ~", round(ess / nw, 1))

# 3. split one chain in half, do the halves come from the same distribution
# KS assumes independent samples, so thin by the acl first or it will reject
# a perfectly good chain
# https://en.wikipedia.org/wiki/Kolmogorov-Smirnov_test
h, t = ns // 2, int(np.ceil(nw * ns / ess))
a, b = par[0, :h:t], par[0, h::t]
print("split-half KS p      ", ks_2samp(a, b).pvalue,
      " on only", len(a), "vs", len(b), "samples")

# 4. walkers started in different places, do their means agree
# the mcse is the error on the pooled mean, so one walker's mean is sqrt(nw)
# worse than that. compare the spread of the walker means to it
# https://python.arviz.org/en/stable/api/generated/arviz.mcse.html
mcse = np.asarray(az.mcse(par)).item()   # arviz returns it wrapped in an array
print("spread of walker means", round(par.mean(axis=1).std(ddof=1), 4),
      " expected", round(mcse * np.sqrt(nw), 4))

# 5. do all walkers spend the same fraction of time within X of the peak
# the one-bin version of test 3. expected scatter is binomial, using the
# effective sample size per walker
peak, X = 0.76, 0.5
frac = (np.abs(par - peak) < X).mean(axis=1)
f = frac.mean()
print("fraction near peak   ", f"{frac.min():.3f} to {frac.max():.3f}",
      " scatter", round(frac.std(ddof=1), 3),
      " expected", round(np.sqrt(f * (1 - f) / (ess / nw)), 3))
