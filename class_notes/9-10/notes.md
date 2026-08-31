# PHY 607 - Class 6 - Thursday, September 10, 2026

**Remote class.** We meet in room 208 as usual; I will join by video.

## Class Outline & Plan

- Numerical error
    - approximation error
      - Euler's method
        - explicit vs implicit integration
      - symplectic integrators
      - just extend to higher orders: Runge-Kutta
        - Euler is only the first-order truncation of the expansion; nothing
          stops us from keeping more terms
        - sampling the slope at more points inside the step buys you order
        - midpoint method (RK2), then the classical RK4
        - you do not need to derive the weights, but you should know what each
          stage is estimating
        - how local and global truncation error scale with step size for
          Euler vs RK2 vs RK4
        - this is what Project 1 asks you to implement
- Reference for today's material
    - [Python Numerical Methods](https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/Index.html),
      chapters 21 / 22
    - (finding and using documentation is its own topic on Sept 15)

## Project 1

Project 1 was introduced on Sept 3; see [the full description](../projects/project1.md).

- **Initial project plan due Sept 15th** — prepare a written summary of your plan
  which we will discuss next Tuesday.
- **Full project due Friday Sept 25th.**
- The material covered today (truncation error and its scaling with step size) is
  directly required by the project report.

## Next class

- Project 1 plan discussion (plans due)
- finding and using documentation
- python environments and packages
