# Finding satisfying assignments for formulas using a SAT solver
#
# (c) Tomi Janhunen, 2019-2022
#
# You may use this code for the course "Introduction to Formal Specification"
# at Tampere University in Autumn 2022.
#
# Publication and redistribution prohibited.
#
# This script calls the "clasp" solver directly -- make it available on PATH

import sys
sys.path.append('/exercise/bin')
sys.path.append('/submission/user/')

from expr import Var
from subprocess import run, PIPE

MAX_CLAUSES=500000

def lookup(formula, newatom, symbols):
    strf = str(formula)
    if strf in symbols:
        id = symbols[strf]
    else:
        id = newatom
        symbols[strf] = id
        newatom +=1
    return id, newatom

def write_clause(clcnt, lits, out = sys.stdout):
    if clcnt <= MAX_CLAUSES:
        for lit in lits:
            print("%s " % (lit), end = "", file = out)
        print("0", file = out)
        return clcnt+1
    else:
        return clcnt

def clausify(formula, newatom, clcnt, symbols, out = sys.stdout): # Unknown
    op = formula.name
    subfs = formula.children
    id = newatom
    newatom += 1
    if op == "-":
        [sub] = subfs
        id2, newatom, clcnt = clausify(sub, newatom, clcnt, symbols, out)
        clcnt = write_clause(clcnt, [-id, -id2], out)
        clcnt = write_clause(clcnt, [id, id2], out)
    elif op == "&":
        newcl = [id]
        for sub in subfs:
            id2, newatom, clcnt = clausify(sub, newatom, clcnt, symbols, out)
            newcl.append(-id2)
            clcnt = write_clause(clcnt, [-id, id2], out)
        clcnt = write_clause(clcnt, newcl, out)
    elif op == "|":
        newcl = [-id]
        for sub in subfs:
            id2, newatom, clcnt = clausify(sub, newatom, clcnt, symbols, out)
            newcl.append(id2)
            clcnt = write_clause(clcnt, [id, -id2], out)
        clcnt = write_clause(clcnt, newcl, out)
    elif op == "->":
        [sub1, sub2] = subfs
        id1, newatom, clcnt = clausify(sub1, newatom, clcnt, symbols, out)
        id2, newatom, clcnt = clausify(sub2, newatom, clcnt, symbols, out)
        clcnt = write_clause(clcnt, [-id, -id1, id2], out)
        clcnt = write_clause(clcnt, [id, id1], out)
        clcnt = write_clause(clcnt, [id, -id2], out)
    elif op == "<->":
        [sub1, sub2] = subfs
        id1, newatom, clnct = clausify(sub1, newatom, clcnt, symbols, out)
        id2, newatom, clcnt = clausify(sub2, newatom, clcnt, symbols, out)
        clcnt = write_clause(clcnt, [-id, -id1, id2], out)
        clcnt = write_clause(clcnt, [-id, id1, -id2], out)
        clcnt = write_clause(clcnt, [id, id1, id2], out)
        clcnt = write_clause(clcnt, [id, -id1, -id2], out)
    else:
        newatom -= 1
        id, newatom = lookup(formula, newatom, symbols)
    return id, newatom, clcnt
    
def falsify(formula, newatom, clcnt, symbols, out = sys.stdout): # False
    op = formula.name
    subfs = formula.children
    if op == "-":
        [sub] = subfs
        return satisfy(sub, newatom, clcnt, symbols, out)
    elif op == "&":
        newcl = []
        for sub in subfs:
            id, newatom, clcnt = clausify(sub, newatom, clcnt, symbols, out)
            newcl.append(-id)
        clcnt = write_clause(clcnt, newcl, out)
    elif op == "|":
        for sub in subfs:
            newatom, clcnt = falsify(sub, newatom, clcnt, symbols, out)
    elif op == "->":
        [sub1, sub2] = subfs
        newatom, clcnt = satisfy(sub1, newatom, clcnt, symbols, out)
        newatom, clcnt = falsify(sub2, newatom, clcnt, symbols, out)
    elif op == "<->":
        [sub1, sub2] = subfs
        id1, newatom, clcnt = clausify(sub1, newatom, clcnt, symbols, out)
        id2, newatom, clcnt = clausify(sub2, newatom, clcnt, symbols, out)
        clcnt = write_clause(clcnt, [-id1, -id2], out)
        clcnt = write_clause(clcnt, [id1, id2], out)
    else:
        id, newatom = lookup(formula, newatom, symbols)
        clcnt = write_clause(clcnt, [-id], out)
    return newatom, clcnt

def satisfy(formula, newatom, clcnt, symbols, out = sys.stdout): # True
    op = formula.name
    subfs = formula.children
    if op == "-":
        [sub] = subfs
        return falsify(sub, newatom, clcnt, symbols, out)
    elif op == "&":
        for sub in subfs:
            newatom, clcnt = satisfy(sub, newatom, clcnt, symbols, out)
    elif op == "|":
        newcl = []
        for sub in subfs:
            id, newatom, clcnt = clausify(sub, newatom, clcnt, symbols, out)
            newcl.append(id)
        clcnt = write_clause(clcnt, newcl, out)
    elif op == "->":
        [sub1, sub2] = subfs
        id1, newatom, clcnt = clausify(sub1, newatom, clcnt, symbols, out)
        id2, newatom, clcnt = clausify(sub2, newatom, clcnt, symbols, out)
        clcnt = write_clause(clcnt, [-id1, id2], out)
    elif op == "<->":
        [sub1, sub2] = subfs
        id1, newatom, clcnt = clausify(sub1, newatom, clcnt, symbols, out)
        id2, newatom, clcnt = clausify(sub2, newatom, clcnt, symbols, out)
        clcnt = write_clause(clcnt, [-id1, id2], out)
        clcnt = write_clause(clcnt, [id1, -id2], out)
    else:
        id, newatom = lookup(formula, newatom, symbols)
        clcnt = write_clause(clcnt, [id], out)
    return newatom, clcnt

def line_count(f):
    for i, l in enumerate(f):
        pass
    return i+1

def satisfy_formulas(formulas):
    status = "unknown"
    model = []
    newatom = 1
    clcnt = 0
    symbols = dict()
    atoms = dict()

    # Generate Tseitin transformation
    f = open("clauses.cnf", 'w')
    newatom, clcnt = satisfy(Var("true"), newatom, clcnt, symbols, f)
    newatom, clcnt = falsify(Var("false"), newatom, clcnt, symbols, f)
    for formula in formulas:
        newatom, clcnt = satisfy(formula, newatom, clcnt, symbols, f)
        if clcnt > MAX_CLAUSES:
            f.close()
            status = "unknown"
            reason = "More than %d clauses!" % MAX_CLAUSES
            return status, reason
    f.close()
    # For reporting numbers of clauses
    # print("%d atoms %d clauses" % (newatom-1, clcnt))
    for atom in symbols:
        atoms[symbols[atom]] = atom
        
    # Produce the final DIMACS file
    f = open("clauses.cnf", 'r')
    cnt = line_count(f)
    df = open("dimacs.cnf", 'w')
    print("p cnf %s %s" % (newatom-1, cnt), file = df)
    f = open("clauses.cnf", 'r')
    for i, line in enumerate(f):
        print("%s" % line, file = df, end="")
    df.close()

    # Run the SAT solver and interpret its output
    s = run(["clasp", "--time-limit=60", "dimacs.cnf"], stdout = PIPE, universal_newlines = True)
    sout = s.stdout
    rval = s.returncode
    if "s UNSATISFIABLE" in sout and rval == 20:
        status = "unsat"
    elif "s SATISFIABLE" in sout and (rval == 10 or rval == 30):
        status = "sat"
        for line in sout.split("\n"):
            if len(line) > 2 and line[0] == 'v' and line[1] == ' ':
                for id in line.split():
                    if id != "v" and id != "0" and int(id)>0:
                        if int(id) in atoms:
                            model.append(atoms[int(id)])
    else:
        status = "unknown"
        model = sout
    return status, model
