# PHY 607 - Class 20 - Tuesday, November 3, 2026

## Class Outline & Plan

* markov chains
    * why sample instead of evaluating on a grid, the n^d problem from
      [../10-6/why_mc.py](../10-6/why_mc.py)
    * the markov property, the next state depends only on the current one
    * metropolis-hastings
        * propose a step from where you are
        * accept with probability p(new) / p(old), always accept if better
        * the normalisation of the posterior cancels, so you never need it
        * a rejected proposal still produces a sample, you record the current
          position again
    * the proposal distribution is yours to choose
        * too small and the chain crawls, too large and nothing is accepted
        * this is the main thing you tune
    * burn-in, autocorrelation
    * [mcmc.py](mcmc.py) - single walker on a 1d posterior

* Project 3 - [../projects/project3.md](../projects/project3.md)
    * groups of 2-3, mcmc on a problem of your choice
    * topic due Thursday Nov 5, validation plan due Tuesday Nov 10
    * the validation plan and how you enact it is what is graded, not the code
    * no AI on the project until the plan is submitted, and the plan itself
      must not be written with AI
    * all changes through PRs, explicitly reviewed by your partner

* using AI properly

## Next class (Thursday Nov 5)

* Project 3 topic due
* likelihood with a known noise model, applied to the fitting data
* ensemble samplers, `emcee`, corner plots
* in-class: write a likelihood and an ensemble mcmc for your model
