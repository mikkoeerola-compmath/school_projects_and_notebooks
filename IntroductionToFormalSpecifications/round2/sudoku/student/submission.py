# STUDENTS: Please do not add or modify import statements!
#
# Check below the points marked with "INSERT YOUR CODE HERE". You
# are supposed to generate the required formulas on the basis of
# descriptions given in the comments.
#
# Please do not modify the code otherwise.

import sys
from math import sqrt as sqrt
from expr import And, Or, Not, Implies, Equivalent, Var, ValT, ValF
from solve import satisfy_formulas

###############################################################################

# The clues are given as triples (x,y,n) meaning that
# number n should appear in the cell (x,y)

# For a cell (x,y) and a number n, a Boolean variable
# value(x,y,n) is supposed to be true iff n appears at
# cell (x,y) in the solution of a Sudoku puzzle

def value(x, y, number):
    return Var("value", [x, y, number])

# Each cell has at least one number

def inCellFormula(dim, x, y):
    return Or([value(x, y, n) for n in range(1,dim+1)])

# Mutual exclusion within column (cells with the same x-coordinate)

def excludeColumnFormula(dim, x, n):
    fs = []
    # To make only the necessary disjunctions
    combs = set(range(2, dim+1))
    for y in range(1, dim+1):
        for r in combs:
            fs.append(Or(Not(value(x, y, n)), Not(value(x, r, n))))
        combs -= {y+1}
    if fs == []:
        return ValT()
    else:
        return And(fs)

# Mutual exclusion within a row (cells with the same y-coordinate)

def excludeRowFormula(dim, y, n):
    fs = []
    # To make only the necessary disjunctions
    combs = set(range(2, dim+1))
    for x in range(1, dim+1):
        for r in combs:
            fs.append(Or(Not(value(x, y, n)), Not(value(r, y, n))))
        combs -= {x+1}
    if fs == []:
        return ValT()
    else:
        return And(fs)

# Mutual exclusion in a sub-area with dimensions sqrt(dim)xsqrt(dim) where
# sx and sy specify the corner (sx,sy) with the lowest coordinate values
# within a sub-area of Sudoku puzzle
#
# If dim=4, the corners of sub-areas are (1,1), (3,1), (1,3), and (3,3).
# The cells involved with (1,1) are: (1,1), (1,2), (2,1) and (2,2). Using
# and index i=1..4: the cells associated with corner (x,y) can be referred
# by (x+(i-1)%2, y+(i-1)//2) where 2 is sqrt(dim).

def excludeAreaFormula(dim, sx, sy, n):
    fs = []
    sd = round(sqrt(dim))
    combs = set(range(2,dim+1))
    for j in range(1,dim+1):
        for i in combs:
            fs.append(Or(Not(value(sx + (j - 1) % sd, sy + (j - 1) // sd, n)),
                        Not(value(sx + (i - 1) % sd, sy + (i - 1) // sd, n))))
        combs -= {j+1}
    if fs == []:
        return ValT()
    else:
        return And(fs)

###############################################################################

class Error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def extractSolution(dim, model):
    nrg = [n for n in range(1,dim+1)]
    sudoku = [[0 for x in range(dim)] for y in range(dim)]

    for x in nrg:
        for y in nrg:
            for n in nrg:
                stratom = str(value(x, y, n))
                if stratom in model:
                    sudoku[x-1][y-1] = n
    return sudoku

def printSolution(dim, values, out = sys.stdout):
    sd = round(sqrt(dim))
    for y in range(dim,0,-1):
        if y%sd == 0 and y//sd < sd:
            out.write('-')
            for i in range(1,dim+sd):
                out.write("--")
            out.write('\n')
        out.write(' ')
        for x in range(1,dim+1):
            out.write("%d " % (values[x-1][y-1]))
            if x%sd == 0 and x//sd < sd:
                out.write("| ")
        out.write('\n')
    return

def checkSolution(dim, hints, sudoku, out = sys.stdout):
    """
    Print (and validate) the solution found 
    """
    sd = round(sqrt(dim))
    assert(isinstance(dim, int) and sd**2 == dim)

    nrg = range(1,dim+1)
        
    # Helper functions
    def p(txt):
        if out: out.write(txt+"\n")

    def difflist(l1, l2):
        for e1 in l1:
            if e1 not in l2:
                return True
        for e2 in l2:
            if e2 not in l1:
                return True
        return False

   # Check hints
    for (x,y,n) in hints:
        if sudoku[x-1][y-1] != n:
            raise Error("Hint (%d,%d,%d) was not respected!" % (x,y,n))
            
    # Other checks are performed later (by the grader)

    # Feel free to add your own checks here
    
    return sudoku

def solveSudoku(dim, hints, out = sys.stdout):
    sqrdim = round(sqrt(dim))
    assert(isinstance(dim, int) and sqrdim*sqrdim == dim)
    nrg = range(1,dim+1)
    
    # Helper functions
    def p(txt):
        if out: out.write(txt+'\n')

    solution = None
    p("---")
    p("Hints: %s" % (hints))
    p("Dimension: %s" % (dim))

    # Create the formulas needed
    formulas = []

    for x in nrg:
        for y in nrg:
            formulas.append(inCellFormula(dim, x, y))
    
    for n in nrg:
        for x in nrg:
            formulas.append(excludeColumnFormula(dim, x, n))
            
    for n in nrg:
        for y in nrg:
            formulas.append(excludeRowFormula(dim, y, n))

    for n in nrg:
        for ax in range(0,sqrdim):
            for ay in range(0,sqrdim):
                formulas.append(excludeAreaFormula(dim, ax*sqrdim+1,
                                                        ay*sqrdim+1, n))
            
    for (x,y,n) in hints:
        formulas.append(value(x,y,n))
 
    # for f in formulas: p(str(f))

    values = []
    result, model = satisfy_formulas(formulas)
    p("The solver says: "+str(result))
    
    if result == "unsat":
        p("No solution possible!")
        status = "nonexistent"

    elif result == "sat":
        p("Model found: "+str(model))
        values = extractSolution(dim, model)
        printSolution(dim, values, out)
        checkSolution(dim, hints, values)
        status = "found"
    else:
        assert(result == "unknown")
        p('"unknown" (with reason "'+ \
          model + \
          '") returned by the solver, aborting!')
        status = "error"

    return (status, values)
