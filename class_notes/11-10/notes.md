# PHY 607 - Class 21 - Thursday, November 5, 2026

## Class Outline & Plan

* demo: claude code
    * what the loop is actually doing
    * where it goes wrong, and how you would catch it

* has your chain converged?
    * look at the trace first, burn-in is usually visible
    * autocorrelation length
    * run several chains from different starting points, compare the variance
      between them to the variance within them (gelman-rubin)
    * What are the properites of a converged chain?
       * Null tests are the only thing we can really do

## Group work: write a metropolis-hastings sampler

In pairs. [../11-3/mcmc.py](../11-3/mcmc.py) is a starting point if you want
one, but writing it yourself is the exercise.

* sample a 1d distribution where you already know the answer
    * check the mean and variance of your samples against the exact values
* vary the proposal width
    * what acceptance rate do you get, and what does the trace look like?
    * too small and too large both fail, in different ways
* find the burn-in by eye, discard it, see if your answer changes
* estimate the autocorrelation length and thin by it
    * how many independent samples did you actually get out of the chain?
    * (look at the example autorcorrelation script)
* Implement an ensemble sampler with 500 walkers
      * Run on the model and data we used for the prior 'fitting' exercise.
      * Plot the distribution of each parameter after 'burn in' 
      * Identify 'burn in' by eye by looking at trace plots (plot of the walker as a function of iteration). 
* Compare your result to using an off the shelf sampler like `emcee`. 


