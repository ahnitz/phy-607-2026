# In-class Exercise: Spring Oscillator

Introduced Tuesday, September 15. Continues Thursday, September 17.

* Implement a spring oscillator
    * Choose your own initial condition (do not choose a case where no evolution occurs)
    * Recall the force equation and substitute into your existing code
* Try the euler explicit, and symplectic forms
* Implement a second order runge kutta algorithm
* Compare the accuracy of all techniques
    * How well is energy conserved over long periods? What are the differences
      between the various methods?

## Follow-up

Determine what the modified hamiltonian is for the 1d spring oscillator when
using the Euler symplectic integrator method.

* *Hint: compare the unmodified energy at each time step. What would you have to
  add to get a conserved form?*
