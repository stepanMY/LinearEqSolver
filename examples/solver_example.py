import numpy as np
from util.solver import LinEqSolver

solver = LinEqSolver()

A, b = np.array([[1, 1], [1, 1]]), np.array([1, 0])
print(solver.solve(A, b))
A, b = np.array([[1, 1, 0], [2, -2, 0], [3, -3, 0]]), np.array([1, 0, 0])
print(solver.solve(A, b))
A, b = np.array([[1, 1, 1], [1, -2, 4], [3, -2, 12]]), np.array([1, 2, 3])
print(solver.solve(A, b))
A, b = np.array([[1, 1], [2, 2], [3, -3]]), np.array([1, 2, 0])
print(solver.solve(A, b))
A, b = np.array([[2, 2, 3, 1, 3], [2, -2, 4, 1, 4], [3, -3, 0, 2, 12]]), np.array([1, 1, 0])
print(solver.solve(A, b))
