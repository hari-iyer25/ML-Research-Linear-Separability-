import polytope as pc
import numpy as np

# Compute convex hulls A and B of "true" points T and "false" points F.
# For each P in T, check if P is in B. Return false if so.
# For each P in F, check if is in A. Return false if so.
# Return true.

def lin_sep(points1, points2, dim):
    if (len(points1) < 1 or len(points2) < 1):
        return True
    #Add dummy points to ensure full dimensionality.
    for i in range(dim):
        newPoint1 = [*points1[0]]
        newPoint1[i] = newPoint1[i] + 0.1
        newPoint2 = [*points2[0]]
        newPoint2[i] = newPoint2[i] + 0.1
        points1.append(tuple(newPoint1))
        points2.append(tuple(newPoint2))
    
    hull1 = pc.qhull(np.array(points1))
    hull2 = pc.qhull(np.array(points2))
    intersection = hull1.intersect(hull2)

    return pc.is_empty(intersection)


'''
points1 = [(1,1,1), (0,0,1),(1,0,0),(0,1,0)]
points2 = [(0, 1, 1), (1, 0, 1), (0, 0, 0),(1,1,0)]
print(lin_sep(points1, points2, 3)) # Should be False
'''
'''
points1 = [(0,0,0), (1,0,0), (0,1,0), (1,1,0)]
points2 = [(0,0,1), (1,0,1), (0,1,1), (1,1,1)]

print(lin_sep(points1, points2, 3)) # Should be True
'''
'''
points1 = [(1,0,0), (0,1,0), (1,0,1), (0,1,1)]
points2 = [(0,0,0), (1,1,0), (1,1,1), (0,0,1)]

print(lin_sep(points1, points2, 3)) # Should be False """

print(lin_sep_sp(points1,points2,3))

'''

points1 = [(1, 2, 1), (2, 2, 2), (1, 3, 1)]
points2 = [(3, 3, 3), (4, 4, 4), (5, 5, 5)]
print(lin_sep(points1, points2, 3))  # Expected output: True

points1 = [(1, 1), (2, 2), (3, 3)]
points2 = [(1, 2), (2, 3), (3, 4)]
print(lin_sep(points1, points2, 2))  # Expected output: False

points1 = [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
points2 = [(0, 0, 1), (1, 1, 1), (2, 2, 2)]
print(lin_sep(points1, points2, 3))  # Expected output: True

points1 = [(1, 1), (2, 2), (3, 3), (4, 4)]
points2 = [(0, 0), (1, 0), (0, 1), (1, 1)]
print(lin_sep(points1, points2, 2))  # Expected output: False

points1 = [(0, 0), (1, 1)]
points2 = [(0, 1), (1, 0)]
print(lin_sep(points1, points2, 2))  # Expected output: True

points1 = [(1, 1), (1, 2), (1, 3)]
points2 = [(2, 1), (2, 2), (2, 3)]
print(lin_sep(points1, points2, 2))  # Expected output: True

# Test the function with provided points
points1 = [(1, 1), (2, 2), (3, 3)]
points2 = [(1, 2), (2, 3), (3, 4)]
print(lin_sep(points1, points2, 2))  # Expected output: TRUE