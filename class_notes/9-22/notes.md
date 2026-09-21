# PHY 607 - Class 9 - Tuesday, September 22, 2026

## Class Outline & Plan

* Discussion of the harmonic oscillator
    * results from the Sept 17 group work: what is the modified Hamiltonian for
      the 1d spring oscillator under symplectic Euler?
    * how did the correction term scale with the time step?
    * why does symplectic Euler conserve a *nearby* quantity rather than the
      true energy.
    * How does the long time behavior compare to a second-order integrator that is not symplectic?

* Numerical precision
    * We have already discussed truncation / aproximation error, this is not the same
    * how a number is actually stored: sign, exponent, finite mantissa
    * representation error with examples, rounding, accumulation

* python types continued
    * tuples, dictionaries, lists
    * `numpy` arrays alongside the built-in types

* classes ([tutorial](https://docs.python.org/3/tutorial/classes.html))
    * why a class, rather than functions plus a dict
    * `__init__`, attributes, methods
    * [inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
      and `super()`
    * special ("dunder") methods
        * operators: `__add__`, `__mul__`, `__eq__`, `__lt__`
        * [operator module reference](https://docs.python.org/3/library/operator.html)

## If time (otherwise Thursday)

* Start on computational complexity
    * time / space
        * best / average / worst
    * what is the computational complexity of common algorithms?
    * search / sort
    * time complexity in python
        * [Python Time & Space Complexity Reference](https://pythoncomplexity.com/)
        * [wiki.python.org TimeComplexity](https://wiki.python.org/moin/TimeComplexity)
          — still accurate, but the wiki is being archived

## Pending time: Project 1 questions
**Project 1 is due Tuesday, September 29.**

Worth checking with me if you are unsure about:

* whether your chosen ODE and integral really have exact solutions
* the truncation error derivation and demonstrating the expected scaling
* what counts as an adequate validation section

## Next class (Thursday Sept 24)
* computational complexity continued
* sorting algorithms and timing
* last class before Project 1 is due
