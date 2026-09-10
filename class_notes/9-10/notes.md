# PHY 607 - Class 6 - Thursday, September 10, 2026

**Remote class.** We meet in room 208 as usual; I will join by video.

## Class Outline & Plan

- Numerical error
    - approximation/truncation error
      - Euler's method
        - local vs global error
        - explicit vs implicit integration
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
       - symplectic integrators (discussed more later)
- Reference for today's material
    - [Python Numerical Methods](https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/Index.html),
      chapters 21 / 22

## Project 1

Project 1 was introduced on Sept 3; see [the full description](../projects/project1.md).

- **Initial project plan due Sept 17th** — prepare a written summary of your plan
  which we will discuss next Thurday
- **Full project due Tuesday Sept 29th.**
- The material covered today (truncation error and its scaling with step size) is
  directly required by the project report.

## Next class

- python environments, modules, and packages
- Project 1 more detailed introduction
- symplectic methods and the harmonic oscillator
