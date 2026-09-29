# PHY 607 - Class 11 - Tuesday, September 29, 2026

* Project 1 is due today
    * short discussion of how it went, common problems

* Project 2 comes Thursday - start thinking about a partner now
    * plan is due Tuesday Oct 6

* profiling
    * [`cProfile`](https://docs.python.org/3/library/profile.html#module-cProfile)
    * `prof.sh` over `example.py` gives `profile.txt`
    * sort by cumulative time, or the real lines sit under the imports
    * the sleep costs more than ten million numpy ops
    * `%timeit` in ipython, or the `timeit` module (`../9-24/timing.py`)

* random numbers
    * pseudorandom, not random - seeds and reproducibility
    * `lcg.py` - `x = (a*x + c) % m`
        * same seed, same sequence
    * `lcg_tests.py` - is it any good?
        * passes: flat histogram, mean 0.5, variance 1/12, no autocorrelation
        * fails: last bit is 0,1,0,1 forever, bit j repeats every 2^(j+1)
        * fails: consecutive pairs lie on a lattice
        * repeats after exactly m values
        * [linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator)
          for the period conditions, the spectral test, RANDU
    * passing the easy tests is not the same as being random
    * `numpy.random`, the generator interface
    * drawing from a distribution
        * inverse CDF
        * rejection sampling
        * `lcg_dist.py` - uniform turned into an exponential and a gaussian,
          each against its pdf

## Rest of class: finish the higher precision type

See [../9-24/highprec.md](../9-24/highprec.md).

* working class, and the algorithm showing where `float` falls over
* bubble sort and merge sort against it, split across the group
* plot sort time vs list length, compare to the expected scaling
* profile it and find the bottleneck
* post the plot and a short summary before Thursday

## Next class (Thursday Oct 1)

* Project 2 introduced - [../projects/project2.md](../projects/project2.md)
* packaging and `black`
* monte-carlo integration, variance reduction, importance sampling
