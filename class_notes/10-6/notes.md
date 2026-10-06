# PHY 607 - Class 13 - Tuesday, October 6, 2026

## Class Outline & Plan

* Project 2 partner and plan due today
    * I will return comments by Thursday morning
    * Fall Break Oct 12-13, so Thursday is the last class before the break

* what monte-carlo integration is - `mc_anim.gif`, `mcint.py`
    * throw darts at a box, count what lands inside
    * the estimate settling into the 1/sqrt(N) funnel

* why bother - `why_mc.py`, `why_mc.png`
    * a grid (midpoint) in d dimensions has error N^(-2/d), monte-carlo has
      N^(-1/2) no matter what d is
    * so the grid wins easily in 1d, and loses badly past d = 4
    * plot shows d=1 and d=8 only: the grid line goes from steepest to
      flattest, the two monte-carlo lines barely differ

* on the board
    * derive the variance of the estimator, where 1/sqrt(N) comes from
    * importance sampling as variance reduction: sample where the integrand is
      large, divide by the proposal
    * rejection sampling: the acceptance fraction is the cost
    * [monte-carlo methods](https://people.duke.edu/~ccc14/sta-663/MonteCarlo.html#monte-carlo-integration)

## Group work: monte-carlo integration

Today and Thursday, see [mc_exercises.md](mc_exercises.md).

## Next class (Thursday Oct 8)

* continue the monte-carlo exercises
* comments back on the Project 2 plans
* last class before Fall Break
