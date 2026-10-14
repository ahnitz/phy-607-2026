# PHY 607 - Class 15 - Thursday, October 15, 2026

## Class Outline & Plan

* review the monte-carlo results you got
    * each group: what did you get for the area, and what uncertainty?
    * did the uncertainty actually scale as N^(-1/2)?
    * how did you handle the circumference, where there is no closed form?

* Project 2
    * individual contributions should be integrated as of today
    * due Thursday Oct 22, so Tuesday is the last class before then
    * questions on packaging, the entry point, numpydoc

* argument parsing
    * `argparse`, so the installed script takes options instead of being edited
    * see `../10-1/example_package/examp/__init__.py`

* optimization
    * brute force / explicit exploration
    * gradient descent
        * how do you get a gradient numerically?
          [finite differences](https://en.wikipedia.org/wiki/Finite_difference_coefficient)
        * choosing a step size, how to make it likely to converge
    * newton's method
        * uses the second derivative, so it needs more per step
    * failure modes
        * local vs global minima
        * narrow curved valleys
    * transforming the problem into an easier one
    * nelder-mead [next class]

## Group work: minimising the Rosenbrock function

Today and Tuesday, see [optimization.md](optimization.md).

## Next class (Tuesday Oct 20)

* nelder-mead
* continue the optimization exercise
* last class before Project 2 is due
