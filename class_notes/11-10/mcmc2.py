import numpy
import tqdm
import numpy.random
from matplotlib import pyplot as plt

def post(x):
    return 1 / (2 * numpy.pi) ** 0.5 * numpy.exp(-1/2 * x ** 2.0) * numpy.sin(2 * x) ** 2.0
   
def proposal2(x):
    return numpy.random.uniform(-1, 1) + x
    
def mcmc(initial, post, prop, iterations):
    x = [initial]
    p = [post(x[-1])]
    for i in tqdm.tqdm(range(iterations)):
        x_test = prop(x[-1])
        p_test = post(x_test)

        acc = p_test / p[-1]
        u = numpy.random.uniform(0, 1)
        if u <= acc:
            x.append(x_test)
            p.append(p_test)
        else:
            # a rejected proposal still gives a sample, you stay put
            x.append(x[-1])
            p.append(p[-1])
    return x, p

def acl(x, b):
    # batch means. if b is much longer than the acl the batch means are
    # independent, so their variance tells you the acl
    m = len(x) // b
    means = x[:m * b].reshape(m, b).mean(axis=1)
    return b * means.var(ddof=1) / x.var(ddof=1)

chain, prob = mcmc(10, post, proposal2, 1000000)
chain = numpy.array(chain)
samples = chain[1000:]

# raise b until the answer stops growing, that plateau is the acl
for b in [20, 100, 500, 2000, 10000]:
    print("b =", b, " acl =", round(acl(samples, b), 1))
print("independent samples:", round(len(samples) / acl(samples, 2000)))

plt.figure()
plt.title("Evolution of the walker")
plt.plot(chain)
plt.ylabel('x-value')
plt.xlabel('Iteration')

plt.figure()
plt.title("Evolution of the walker")
plt.plot(chain)
plt.xlim(0, 500)
plt.ylabel('x-value')
plt.xlabel('Iteration')

plt.figure()
plt.title("Posterior samples")
_ = plt.hist(samples[::100], bins=100)

plt.show()
