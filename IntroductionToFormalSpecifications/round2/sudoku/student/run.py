# This script runs all test instances
#
# USAGE: python run.py

from expr import *
from puzzles import testPuzzles
from submission import solveSudoku
import sys

if __name__ == '__main__':
    
    for (dim, hints, _) in testPuzzles:
        solveSudoku(dim, hints, sys.stdout)
