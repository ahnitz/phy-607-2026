# Group Exercise: Fitting a Model to Data

Today and continuing next class, in groups of 3.

The data is in `data.hdf`, loaded by [read_data.py](read_data.py). Plot it
first and look at it before deciding anything.

* (1) each group member develops a *different* model for the data
    * each model must have at least 4 parameters
* (2) each person fits their model using one of the minimizers you wrote for
  the Rosenbrock exercise
    * least squares, so you are minimising the sum of squared residuals
    * this is the same optimization problem, only now in parameter space
* (3) test the goodness of fit with the adjusted R^2 [next class]
* (4) compare how well each model in the group fits the data

## Worth thinking about

* which minimizer handled parameter space well, and did that match how it
  handled Rosenbrock?
* how sensitive is your best fit to where you started the minimizer?
