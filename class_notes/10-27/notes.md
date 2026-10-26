# PHY 607 - Class 18 - Tuesday, October 27, 2026

## Class Outline & Plan

* where each group got to on the fitting exercise
    * what model did each person pick, and did the minimizer find it?

* goodness of fit
    * residuals and the sum of squared residuals
    * [R^2](https://en.wikipedia.org/wiki/Coefficient_of_determination),
      what fraction of the variance the model accounts for
    * adding parameters can only reduce the sum of squared residuals, so R^2
      alone always prefers the bigger model
    * adjusted R^2 penalising the number of parameters

* incorporating noise in your model
    * a best fit value is a single number, what you want is a distribution
    * resampling and
      [bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics))
    * propagation of errors, which requires assuming a noise model

## Group work: fitting a model to data

Continue [../10-22/fitting.md](../10-22/fitting.md), now including the
goodness of fit step.

* compare the models within your group using adjusted R^2
* does the ranking change if you use plain R^2?

## Next class (Thursday Oct 29)

* bayes theorem, likelihood functions
* markov chains
* Project 3
