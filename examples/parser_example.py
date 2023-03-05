from util.parser import EqParser
from util.solver import LinEqSolver

parser = EqParser()
solver = LinEqSolver()

example = '''2x+3.3y+54 f -  12z = 12.5, 
45x+1. 45y=12,          2y+ 3 x = 1,
45f+32x=0'''
A, b = parser.parse_eqs(example)
print(A, b)
n_sol, sol = solver.solve(A, b)
print(n_sol, sol)

example = '''
a + 2b + 3c=3, 
-2b+c+a=2,          
-a+0.3b+4c= 1,
12d+4a+3c-b=0
'''
A, b = parser.parse_eqs(example)
print(A, b)
n_sol, sol = solver.solve(A, b)
print(n_sol, sol)
