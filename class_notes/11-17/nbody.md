# In-Class Project: N-Body Simulation of Drag

Starts Tuesday November 17, continues Thursday Nov 19 and Tuesday Dec 1.

Build a primitive n-body simulation of a projectile moving through a fluid of
particles, and measure the drag that results.

> **AI is allowed on the implementation, but not before the plan exists.**
> The pseudocode and the validation plan are written by your group, without
> AI, and reviewed together before anyone writes code.

## (1) Plan first, as a group, no AI

* agree what you are simulating
    * number of fluid particles, mass and size of the projectile, initial
      conditions, boundary conditions
* pseudocode for the main loop
    * what modules do you need, what are the function interfaces, what does
      each one return
* the validation plan
    * what should be conserved, and under what settings
    * what limit has an answer you already know
        * no fluid particles, does the projectile travel ballistically?
        * elastic collisions only, is energy conserved?
    * what would tell you the simulation is wrong
* read the plan out to each other before you start. if one person cannot
  explain a test, it is not a test yet

## (2) Divide the work

* high-level analysis script, sets up the system, runs the loop, collects data
* post-processing and plotting, trajectory, velocity and drag force over time
* core modules, forces between particles, position and velocity updates,
  boundary conditions
* tests, the force calculation and the stability of the integration

## (3) Implement

* AI is permitted from here, with disclosure
    * record which tools were used, on which parts, for what purpose
* you are responsible for everything you submit, a mistake by the AI is your
  mistake
* run your own validation plan as you go, and revise it when a test turns out
  to be uninformative

## The result

* measure the drag force on the projectile and how it depends on something
  you choose, speed, projectile size, or fluid density
* compare it to what you expected before you ran it
