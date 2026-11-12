# PHY 607 - Class 23 - Thursday, November 12, 2026

## Class Outline & Plan

* Project 3 is due Tuesday Nov 17

* convergence tests
    * gelman-rubin
    * autocorrelation length, per parameter
    * split one chain in half, do both halves give the same posterior
        * How does one measure 'same'? 
    * start from different places, do they agree?
    * Walkers all pass within X of the peak at the same fractional rate

* comparing two models
    * more parameters always fits better, the same problem as R^2
    * what you can say from the posterior
        * do the parameter intervals overlap zero?
        * are any two parameters so correlated that the model is degenerate?
    * what a corner plot tells you that a table of best-fit values does not

## Group work: multi-walker mcmc on the fitted data

* (1) write the likelihood for the fitting data
    * gaussian noise likelihood
    * your choice of priors
* (2) run your own model with many walkers
    * say 100-500, start from random initial positions
    * trace plot per parameter, identify burn-in by eye
* (3) corner plot from the walkers after burn-in
    * `pip install -r ../11-10/requirements.txt`
    * does the peak sit where your minimizer put the best fit?
    * Are there correlated parameters? 
* (4) pick one convergence test from the list above and apply it
    * different individuals take different ones, compare within your group
* (5) if there is time, run the same model through `emcee`

## Next class (Tuesday Nov 17)

* Project 3 due
* Project 4 introduced
* start of n-body / fine element analyses
