
This zipfile contains the base code for the programming assignment
"Sudoku Solver". Please see the related course material for an
introduction to this problem.  The code consists of the following
Python sources:

- README.txt: This file
- expr.py: Constructors (Z3 style) for propositional formulas
- puzzles.py: Some sample instances of the problem
- run.py: Simple script for running the test instances
- solve.py: Translating formulas to clauses, calling the SAT solver,
            and interpreting satisfying assignments in symbols
- submission.py: Encoding the Sudoku problem in propositional logic

Note that the constructors of the formulas can be used very
flexibly. In particular, And(.) and Or(.) accept a _list_ of
arguments. Thus, it is possible to exploit list comprehensions of
Python to generate and/or-statements of varying length. A couple of
examples follow (unrelated with the actual solution of this exercise):

# Demo of formula constructors
import sys
from expr import And, Or, Not, Implies, Equivalent, Var
from submission import value
n=4
formulas = []
# Fixed number of arguments
for x in range(1,n):
    formulas.append(Or(Not(value(x,1,1)),Not(value(x+1,1,1))))
# Varying number of arguments (using list comprehension, see [...] inside)
for x in range(1,n+1):
    formulas.append(Or([value(x,y,1) for y in range(1,n+1)]))
# Print to see the outcome
for formula in formulas:
    print(formula)

You may run the test instances from command line as follows:

$ python run.py

However, since the functions in submission.py return "true" for
every formula, the solutions found do not satisfy the requirements
of the Sudoku problem. Thus, error messages will be generated until
the required formulas have been encoded in submission.py.

We strongly recommend to use/install Clasp for testing purposes; the
latest versions are available at https://potassco.org/. You may also
use the script wget-clingo.sh to download the required binaries.  It
is easiest if you set Clasp accessible from the command line by the
command "clasp". Alternatively, you may declare the exact location of
Clasp in the file solve.py. If you are interested in the numerous
options of Clasp, please call it with the option flag --help or
the flag --help=n where n=1,2,3 gives the level of detail.




