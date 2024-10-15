import numpy as np
from scipy.optimize import linprog

def lin_sep(points1, points2, dim):
    
    # Coefficients for the objective function (we'll use a dummy objective of 0's since we only care about feasibility)
    c = np.zeros(dim + 1)

    A_ub = []
    b_ub = []

    #appending the the form A_ub @ x <= b_ub

    for point in points1:
        #w^T * x + b >= 1 -> -(w^T * x + b) <= -1 -> -w^T * x - b <= -1
        A_ub.append([-x for x in point] + [-1])
        b_ub.append(-1)
    
    for point in points2:
        # -(w^T * x + b) >= 1 -> w^T * x + b <= -1
        A_ub.append([x for x in point] + [1])
        b_ub.append(-1)
    
    A_ub = np.array(A_ub)
    b_ub = np.array(b_ub)

    # Solve the linear program
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(None, None))

    # Check if the optimization problem is feasible
    return result.success

# Test the function with provided points
points1 = [(1, 1), (2, 2), (3, 3)]
points2 = [(1, 2), (2, 3), (3, 4)]
print(lin_sep(points1, points2, 2))  # Expected output: TRUE
