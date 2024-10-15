from cnfgen import RandomKCNF
from pysat.solvers import Minisat22
import nnf.dimacs
import io

#Variables labeled as integers from 1 to n in the formula. -1 is "not" 1 

#function for satisfiability
def is_satisfiable(formula):
    solver = Minisat22()
    for clause in formula:
        solver.add_clause(clause)
    result = solver.solve()
    if result:
        #if true, return assignment
        satisfying_assignment = solver.get_model()
        solver.delete()  
        return True, satisfying_assignment
    else:
        solver.delete() 
        return False, None
    
def is_satisfying(formula, assignment):
    assignment_dict = {key: value for key, value in zip(range(1,formula.number_of_variables() + 1), assignment)}
    #print(f"\n \n  LINSEP {assignment} \n")
    return CNF_to_NNF(formula).satisfied_by(assignment_dict)

#function to check trivial/non-trivial
def is_nontrivial(formula):
    solver = Minisat22()
    
    for clause in formula:
        solver.add_clause(clause)

    if not solver.solve():
        solver.delete()
        return False

    first_solution = solver.get_model()

    block_clause = [-lit for lit in first_solution]
    solver.add_clause(block_clause)

    nonTrivial = solver.solve()
    solver.delete()
    return nonTrivial

def count_satisfying_assignments(formula):
    solver = Minisat22()
    
    for clause in formula:
        solver.add_clause(clause)

    count = 0
    while solver.solve():
        solution = solver.get_model()
        #print(f"Satisfying Assignment {count + 1}: {solution}")
        block_clause = [-lit for lit in solution]
        solver.add_clause(block_clause)
        count += 1

    solver.delete()
    return count

#function to generate random ksat formula, k can be changed 
def generate_random_ksat(num_vars, num_clauses, k=3):
    formula = RandomKCNF(k, num_vars, num_clauses)
    return formula

def generate_unsat_ksat(num_vars, num_clauses, k=3):
    solver = Minisat22()
    formula = generate_random_ksat(num_vars, num_clauses, k)

    for clause in formula:
        solver.add_clause(clause)
    
    while solver.solve():
        solution = solver.get_model()
        block_clause = [-lit for lit in solution]
        solver.add_clause(block_clause)
        formula.add_clause(block_clause)

    return formula

#function to return the clauses in the formula
def get_clauses(formula):
    return [list(clause) for clause in formula]

def CNF_to_NNF(formula):
    with io.StringIO() as f:
        f.write(formula.to_dimacs())
        f.seek(0)
        return nnf.dimacs.load(f)
    
#ksat = generate_random_ksat(4, 3)
#print(get_clauses(ksat))
#num_solutions = count_satisfying_assignments(ksat)
#print(f"Number of Satisfying Assignments: {num_solutions}")
#print(is_satisfying(ksat, {1: True, 2: True, 3: True, 4: True}))


