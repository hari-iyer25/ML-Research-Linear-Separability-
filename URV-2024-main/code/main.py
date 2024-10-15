from lin_sep import lin_sep
from sat_tools import generate_random_ksat, is_satisfying, count_satisfying_assignments, generate_unsat_ksat
from dimacs_to_latex import dimacs_to_latex
from cnfgen import CNF
import time
import sqlite3
import random
import db
from multiprocessing import Process

#Globals
START = time.time()
num_formulas = 1
i = 1

db = sqlite3.connect("./db/SAT.sqlite")
cursor = db.cursor()

def main():
    global i
    num_vars = random.randint(3, 6)
    num_clauses = random.randint(num_vars, num_vars * 2)
    curr_assignment =  [0 for i in range(num_vars)]

    true_points = []
    false_points = [] 
    formula = CNF()
    
    #Methods
    def gen_point_sets(n = 0): #Idea here is to generate all 2^n possibilities for literal_values. Recursion possibly?
        nonlocal num_vars, curr_assignment
        if n == num_vars:
            handle_point(curr_assignment.copy())
            return
        else: # Recur with variable n set to 0, then recur with variable n set to 1
            gen_point_sets(n + 1)
            curr_assignment[n] = 1
            gen_point_sets(n + 1)
            curr_assignment[n] = 0 #Backtrack
        
    def handle_point(point): #Potentially usful helper method--append point to appropriate set.
        nonlocal true_points, false_points, formula
        if (is_satisfying(formula, point)):
            true_points.append(tuple(point))
        else:
            false_points.append(tuple(point))

    def get_linsep_formula():
        nonlocal true_points, false_points, formula, num_clauses, num_vars
        while (True):
            formula = generate_random_ksat(num_vars, num_clauses)
            #print(f"\n \n  LINSEP {formula.number_of_variables()} {num_vars} \n")
            gen_point_sets()
            if (lin_sep(true_points, false_points, num_vars)):
                true_points = []
                false_points = []
                return formula
            else:
                true_points = []
                false_points = []

    def get_unsat_formula():
        nonlocal num_vars, num_clauses, formula
        formula = generate_unsat_ksat(num_vars, num_clauses)
        return formula

    def get_sat_formula():
        nonlocal formula, num_vars, num_clauses
        formula = generate_random_ksat(num_vars, num_clauses)
        while (count_satisfying_assignments(formula) == 0):
            formula = generate_random_ksat(num_vars, num_clauses)
        return formula
    """
    formula = get_unsat_formula()
    num_clauses = formula.number_of_clauses()
    num_sols = 0
    print(f"FOUND UNSAT FORMULA {i}")
    cursor.execute(f"INSERT INTO unsat_formulas VALUES ('{formula.to_dimacs()}', {num_vars}, {num_clauses}, {num_sols})")

    num_vars = random.randint(3, 6) #EDIT
    num_clauses = random.randint(num_vars, num_vars * 2) #EDIT
    curr_assignment =  [0 for i in range(num_vars)]
    
    formula = get_sat_formula()
    num_sols = count_satisfying_assignments(formula)
    print(f"FOUND SAT FORMULA {i}")
    cursor.execute(f"INSERT INTO sat_formulas VALUES ('{formula.to_dimacs()}', {num_vars}, {num_clauses}, {num_sols})")
    """

    num_vars = random.randint(3, 6) #EDIT
    num_clauses = random.randint(num_vars, num_vars * 2) #EDIT
    curr_assignment =  [0 for i in range(num_vars)]
    
    formula = get_linsep_formula()
    num_sols = count_satisfying_assignments(formula) 
    print(f"FOUND LINSEP FORMULA {i}") #Track progress in terminal. 
    cursor.execute(f"INSERT INTO linsep_formulas VALUES ('{formula.to_dimacs()}', {num_vars},  {num_clauses}, {num_sols})")
    i += 1
    db.commit()


for i in range(num_formulas):
    main()

dimacs_to_latex()

END = time.time()
print(f"ELAPSED TIME: {END - START} seconds")


