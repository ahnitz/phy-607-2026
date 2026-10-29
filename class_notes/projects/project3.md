# Project 3 Description

**Introduced: Thursday, October 29**
**Topic due: Thursday, November 5**
**Validation plan due: Tuesday, November 10**
**Full project and report due: Tuesday, November 17**

This project introduces the use of AI coding tools, specifically Claude Code
and the Claude desktop app. The implementation may be written with them. You will
be primarily assessed on your validation plan and how you iterated on its application.
AI is not permitted for the preparation of the validation plan nor the final
report itself.

> **You are responsible for everything you submit.** Any mistake made by the
> AI is your mistake. You must be able to explain and defend any part of the
> code and the results, whether or not a tool produced them. You must disclose
> the exact manner of use: which tools, on which parts of the work, and for
> what purpose. A vague acknowledgement is not sufficient.

## What is graded

The primary basis for your grade is the validation plan and how you iterate on
the execution of the plan along with your account of both in the report.
Working code that meets the technical  requirements below is expected,
but the code itself is not what is being assessed. A project with a correct 
result and a thin validation plan will score below one with a thorough plan 
that uncovered and corrected a problem.

## The validation plan

**No AI use on this project until the validation plan is submitted, and the
plan itself must not be written with AI.** It is your own work, the same as
Projects 1 and 2. It is much harder to write a useful test for something after 
you have watched a tool produce it. 

* commit the plan to the repository as a file before any AI-assisted commit
    * the git history is the evidence of the ordering, so make the commit
      before you start
    * later revisions go in as further commits, which is also the evidence of
      iteration
    * revisions made after Nov 10 may use AI, as long as you say so and the
      original is still in the history
* the plan should state, before any implementation exists
    * what the code is supposed to do, precisely enough to test
    * what you would accept as evidence that it is correct
    * what results might tell you it is wrong
* the tests themselves should be executable where that is possible
* candidate validation methods for an mcmc
    * a case with a known analytic answer, to check you recover it
    * injecting known parameters into simulated data and recovering them
    * symmetries and degeneracies in the model, which should appear in the
      posterior
    * convergence diagnostics (see the technical requirements)
    * the hand written sampler against the off the shelf one
* iterate
    * when a test fails or turns out to be uninformative, revise the plan
    * record what changed and why, in the git commits and in the report

## Timeline

* By Nov 5, decide your partner and your topic, and submit a short
  description of the problem, the parameter space, and what you expect the
  posterior to look like.
* By Nov 10, submit the validation plan, written without AI. This is the point
  AI use becomes permitted, so nothing before it may be AI assisted.
* Nov 17, full project and report are due.

The implementation window is deliberately short. The time before Nov 10 goes
into deciding what correct means for your problem.

## Conceptual elements

* Will be done in groups of 2-3
* write a single report & submit a single git repository with the developed code
* In this project you will use Markov Chain Monte Carlo methods to sample
  from a multidimensional distribution.
* You should choose a statistical problem with a non-trivial parameter space.
    * It may be an analysis of some data using Bayesian Inference
      or the exploration of a multi-dimensional distribution
      from elsewhere in physics (for example, the 2d ising model,
      quantum mechanics).
    * You are welcome to use actual research problems if you have them.
* A key requirement is to choose carefully the parameters of your algorithm.
  You should motivate your choice of proposal function, examine the correlation
  of your samples, and think critically about the effect on your results of
  parameters such as burn-in period, total iterations, and autocorrelation
  length. You should discuss your choices in your report.

## Review requirements

* all changes must be made through pull requests
    * no direct commits to the main branch
* you must review your own code before opening the pull request
* every pull request must be explicitly reviewed by your partner before it is
  merged
    * your partner must investigate the change themselves, not just approve it
    * your partner must suggest changes where they see a problem
    * this applies to AI generated changes exactly as it does to your own
* the reviews must be in writing on the pull requests themselves

## Technical

These are requirements, but they are not the primary basis of the grade.

* The code should be in a new git repository shared between the group members
* write a single python package (installable) with included main script that
  runs the simulation
    * https://packaging.python.org/en/latest/tutorials/packaging-projects/
      https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata
    * The main script should be installed along with the package.
    * The package should list its dependencies needed to run the package
* use numpy / scipy where applicable
    * make use of elementwise array operations
* must follow pep8 style (use black to help enforce style)
* functions / classes / modules must be documented following numpydoc format
    * https://numpydoc.readthedocs.io/en/latest/format.html
* comments should still be used to document pieces of the algorithm within
  functions / methods / etc.
* use git for your development.
    * incremental changes and work by each group member should be evident from
      the history of git commits. Do not simply upload files at the end.
      Develop in git.
    * both members must contribute roughly equally
* you should compare two methods for estimating the model parameters
    * (1) a hand written mcmc
    * (2) an off the shelf implementation from a library of choice
      (e.g. emcee or others)
* You must implement methods to validate that your mcmc chain
  has either converged or is self consistent. You should pick at
  least two methods of convergence testing. One may be informal
  (see https://www.statlect.com/fundamentals-of-statistics/Markov-Chain-Monte-Carlo-diagnostics),
  but at least one should provide a numerical metric (e.g. Gelman Rubin).
  (see https://bookdown.org/rdpeng/advstatcomp/monitoring-convergence.html)

## Report

The validation plan gets its own section, separate from the results.

* that section should contain
    * the plan as you first wrote it, before any implementation
    * every revision you made to it, and what prompted each one
    * what each test actually told you
    * anything the testing caught, including anything an AI tool got wrong
* the AI disclosure, and a short account of how the partner review worked in
  practice
* The report should detail the problem being simulated (e.g. highlighting the
  high-level algorithm, choice of proposal, model, priors where relevant).
* It should be written using latex in a scientific format, formatted similar
  to a scientific paper with clear sections.
* Detail the properties of the samples produced by your analysis
* There should be an explicit validation section that discusses
  and provides evidence that the results are consistent with expectation.
  This should be reasoned based on your critical analysis of the problem
  at hand and the chosen model itself. For example, if your model
  has symmetries or parameter degeneracies, are these represented in the
  result?
* You should also separately validate that the MCMC is consistent with
  having converged. Compare your hand written mcmc and the off
  the shelf method.
    * At least one method should pass your validation tests. If one fails you
      should critically analyze why this may have occured.
