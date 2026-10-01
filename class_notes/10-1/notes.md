# PHY 607 - Class 12 - Thursday, October 1, 2026

## Class Outline & Plan

* Project 1 discussion
    * common problems from the submissions

* Project 2 introduced - see [../projects/project2.md](../projects/project2.md)
    * groups of 2-3, partner and plan due Tuesday Oct 6
    * walk through the technical requirements, several are things we have not
      done yet
    * Fall Break Oct 12-13 sits in the middle of this project

* python packaging - required for Project 2, not covered yet
    * walk through example package
    * [packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/),
      [writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
    * `requirements.txt` vs package dependencies

* style, for real this time
    * `black ugly.py` - run it and diff
    * `black --check` / `black --diff`
    * [numpydoc format](https://numpydoc.readthedocs.io/en/latest/format.html)
      (required for Project 2)

* monte-carlo, the idea
    * why sample instead of putting down a grid
    * error goes as 1/sqrt(N), independent of dimension

* variance reduction [next class]
    * where the 1/sqrt(N) prefactor comes from
    * rejection sampling: the acceptance fraction is the cost
    * importance sampling: sample where the integrand is large
    * the exercise is Tuesday, see [mc_ellipse.md](mc_ellipse.md)

## Group work: start Project 2

The plan is due Tuesday, so use the time now rather than over the weekend.

* pair up and agree on a concept
* sketch the simulation and the high-level pseudocode
* decide who writes what
* scaffold the repo as an installable package while packaging is fresh
* if the higher precision type is still unfinished, take this time for it
  instead

## Next class (Tuesday Oct 6)

* Project 2 partner and plan due
* monte-carlo integration exercises
* more on packaging
