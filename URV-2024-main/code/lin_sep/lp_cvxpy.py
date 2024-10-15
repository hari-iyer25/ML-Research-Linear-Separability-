#might take a while to run

#may require pip install for cvxpy
from cvxpy import Problem, Minimize, norm, Variable, OPTIMAL

def lin_sep(points1, points2, dim):

    # Define the optimization variables
    w = Variable(dim)
    b = Variable()

    constraints = []
    for point in points1:
        constraints.append(w @ point + b >= 1)
    for point in points2:
        constraints.append(w @ point + b <= -1)

    # Define the problem (we use a dummy objective, since we're only interested in feasibility)
    problem = Problem(Minimize(norm(w, 1)), constraints)

    problem.solve()
    
    return problem.status == OPTIMAL

# Example usage
points1 = [(1, 1, 1), (0, 0, 1), (1, 0, 0), (0, 1, 0)]
points2 = [(0, 1, 1), (1, 0, 1), (0, 0, 0), (1, 1, 0)]
print(lin_sep(points1, points2, 3))  # Should be False

points1 = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]
points2 = [(0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
print(lin_sep(points1, points2, 3))  # Should be True

points1 = [(1, 0, 0), (0, 1, 0), (1, 0, 1), (0, 1, 1)]
points2 = [(0, 0, 0), (1, 1, 0), (1, 1, 1), (0, 0, 1)]
print(lin_sep(points1, points2, 3))  # Should be False


