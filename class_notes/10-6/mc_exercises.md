# Group Exercise: Monte-Carlo Integration

Today and Thursday, in groups of 2-3. If your group gets stuck, talk to another
group.

Discuss how you will do each calculation and write the pseudocode before
implementing.

First decide how you will estimate the uncertainty on an integral for a given
N. If you run the estimate many times with independent random numbers, each
estimate is itself unbiased, so the spread of those estimates gives you the
uncertainty.

## (1) The exponential, where you already know the answer

Everything here uses the same function, `exp(-x)` on 0 to 1, so every step can
be checked against the exact answer.

* integrate it two ways
    * mean value: average `f(x)` over uniform samples, times the interval
    * hit or miss: sample a box and count what lands under the curve
* estimate the uncertainty on each, and verify it scales as N^(-1/2)
* which of the two is more efficient at fixed N, and why?
* now draw samples *from* it rather than integrating it, two ways
    * inverse CDF
    * rejection sampling from a uniform
    * check the samples follow the pdf
* hit or miss / rejection sampling are the same accept/reject step put to two
  different uses

## (2) The ellipse, where you do not

Ellipse parameters `a = 5`, `b = 2`.

* area of the ellipse
    * compare to the analytic answer
    * verify that the uncertainty scales as N^(-1/2)
* circumference of the ellipse
    * no elementary closed form, use `scipy.special.ellipe` as the check
* plot the statistical uncertainty against the number of samples
* what improves the overall efficiency without changing the scaling with N?
    * compare a naive proposal, say uniform over the whole space, against one
      you design to reduce the variance

## Reference

* [monte-carlo integration](https://people.duke.edu/~ccc14/sta-663/MonteCarlo.html#monte-carlo-integration)
