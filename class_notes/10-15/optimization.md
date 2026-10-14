# Group Exercise: Minimising the Rosenbrock Function

Today and Tuesday Oct 20, in groups.

Find the minimum of the 2-d Rosenbrock function, which is 0 at (1, 1). Use
[rosen.py](rosen.py) to see how to generate it with scipy, and use the same
ranges as that script: x in (-2, 2), y in (-1, 3).

* implement each of these yourself
    * brute force / explicit exploration of the grid
    * gradient descent, with the gradient from finite differences
    * newton's method
    * nelder-mead [Tuesday]
* start each method from each of the 4 corners of the range
    * how many iterations does each take to get within 1e-10 of 0?
    * does any of them get stuck somewhere that is not the minimum?
* for gradient descent, try several step size scale factors
    * how does the choice change the convergence?
    * what happens when it is too large?
* plot the path each method traverses, for everything except brute force
    * compare the paths. Why does gradient descent take the route it does?

## Things worth noticing

* how many function evaluations does each method need, not just iterations?
  brute force and newton's method pay very differently per step
* the valley floor of the Rosenbrock function is curved, which is the whole
  reason it is a standard test case
