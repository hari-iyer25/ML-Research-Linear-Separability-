import numpy as np

def lin_sep(A,B, dim):

    #compute the geometric difference
    '''
    c = []


    for a in A:
        for b in B:
            diff = tuple(np.subtract(a, b))
            c.append(diff)
    '''

    A = np.asarray(A)
    B = np.asarray(B)

    # Get the number of segments in A and B
    n_A, m = A.shape
    n_B, _ = B.shape

    # Compute all differences using broadcasting
    A_expanded = A[:, np.newaxis, :]  # Shape (n_A, 1, m)
    B_expanded = B[np.newaxis, :, :]  # Shape (1, n_B, m)

    c = A_expanded - B_expanded  # Shape (n_A, n_B, m)
    c = c.reshape(-1, m)

    #origin poin
    #o = np.zeros_like(c[0])

    MCB = []
    for point in c:
        dir_norm = np.linalg.norm(point)
        #to prevent division by 0
        if dir_norm == 0:
            continue
        ray_direction = point/dir_norm
        MCB.append(ray_direction)

    MCB = np.array(MCB)
    # avg of all points in M for the center of the MCB
    oM = np.mean(MCB, axis=0)
    # finds the max radius from the center of MCB to the points on the MCB sphere
    rM = np.max(np.linalg.norm(MCB - oM, axis=1))

    if rM < 1: #1 is the arbitrary radius
        return True
    return False

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

