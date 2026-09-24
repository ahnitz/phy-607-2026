# PHY 607 - Class 10 - Thursday, September 24, 2026

## Class Outline & Plan

* python environments
    * `venv` ([tutorial](https://docs.python.org/3/tutorial/venv.html),
      [reference](https://docs.python.org/3/library/venv.html))
        * `python3 -m venv env`, `source env/bin/activate`, `deactivate`
        * `pip freeze > requirements.txt` / `pip install -r requirements.txt`
    * `conda` ([getting started](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html),
      [cheat sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html))
        * `conda create --name phy607 python numpy scipy matplotlib`
        * `conda activate phy607`, `conda env export > environment.yml`
        * handles non-python dependencies
        * install via [Miniforge](https://conda-forge.org/download) — Miniconda

* computational complexity
    * time / space
        * best / average / worst
    * complexity of common operations — depends on the data structure
        * [pythoncomplexity.com](https://pythoncomplexity.com/),
          [wiki.python.org](https://wiki.python.org/moin/TimeComplexity) (archived)
    * sorting
        * bubble, insertion — O(n^2)
        * merge — O(n log n)
        * bogo — O(n * n!)
    * search: linear vs binary
    * timing
        * `%timeit` in ipython, or the
          [`timeit`](https://docs.python.org/3/library/timeit.html) module
        * `timing.py` — `x in list` vs `x in set`, 40000x apart at n = 1e6
    * profiling
        * [`cProfile`](https://docs.python.org/3/library/profile.html#module-cProfile)
        * `example.py` + `prof.sh` → `profile.txt`, and a call graph png
        * the sleep costs more than ten million numpy ops
    * scaling without deriving the algorithm — `scaling_demo.py`
        * FFT vs naive DFT: speedup grows like n/log n
        * Strassen: 7 block multiplies instead of 8, n^2.807 not n^3

## Group work: higher precision data type

In groups, see [highprec.md](highprec.md).

## Project 1

Due Tuesday, September 29. Last class before then.

* list any dependencies in your README / `requirements.txt`
* last call for questions on truncation error or the validation section

## Next class (Tuesday Sept 29)

* Project 1 due
* Project 2 introduced
* monte-carlo methods and random numbers
    * pseudorandom numbers
    * inverse CDF, rejection sampling
