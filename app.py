import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from util.parser import EqParser
from util.solver import LinEqSolver
from randomizer.sampler import EqSampler


def prepare_output(n_sol, sol, mapping, digits=3):
    """
    Prepare and beautify output

    @param n_sol: string, string in {'none','inf','only'}
    @param sol: np.array, solution of system
    @param mapping: dict, dictionary that contains place in sol-variable_name pairs
    @param digits: int, number of digits to round answers to
    """
    if n_sol == 'none':
        return 'Zero solutions'
    if n_sol == 'inf':
        return 'Infinite number of solutions'
    result = ''
    for i in range(sol.shape[0]):
        if i == (sol.shape[0]-1):
            result += f'{mapping[i]}={round(sol[i], digits)}'
        else:
            result += f'{mapping[i]}={round(sol[i], digits)},\n'
    return result


def solve_eq():
    """
    Solve system of linear equations
    """
    input_val = eqs_fld.get('1.0', 'end-1c')
    try:
        a, b, mapping = parser.parse_eqs(input_val)
        mapping_inv = {mapping[key]: key for key in mapping}
    except:
        res_fld.configure(state='normal')
        res_fld.delete('1.0', 'end-1c')
        res_fld.insert(tk.INSERT, 'Input is incorrect')
        res_fld.configure(state='disabled')
        return
    try:
        n_sol, sol = solver.solve(a, b)
    except:
        res_fld.configure(state='normal')
        res_fld.delete('1.0', 'end-1c')
        res_fld.insert(tk.INSERT, 'System is not specified correctly')
        res_fld.configure(state='disabled')
        return
    res_fld.configure(state='normal')
    res_fld.delete('1.0', 'end-1c')
    res_fld.insert(tk.INSERT, prepare_output(n_sol, sol, mapping_inv))
    res_fld.configure(state='disabled')


def sample_eq():
    """
    Generate system of linear equations
    """
    result = sampler.generate_equations(n_equations, coefficients, n_variables, answers)
    eqs_fld.delete('1.0', 'end-1c')
    eqs_fld.insert(tk.INSERT, ',\n'.join(result))


parser = EqParser()
solver = LinEqSolver()
sampler = EqSampler(15)
n_equations = [3, 4, 5, 6]
coefficients = [-5, -1, -0.66, -0.5, -0.25, 0.25, 0.5, 0.66, 1, 5]
n_variables = [3, 4, 5]
answers = [-3, -1.5, -1, 0, 1, 1.5, 3]

gui = tk.Tk()
gui.geometry('800x400')

eqs_fld = ScrolledText(gui, height=10, width=40)
eqs_fld.place(x=5, y=150)

res_fld = ScrolledText(gui, height=10, width=30, state='disabled')
res_fld.place(x=500, y=150)

btn_solve = tk.Button(gui, text='solve', fg='blue', height=5, width=10, command=solve_eq)
btn_solve.place(x=380, y=100)

btn_generate = tk.Button(gui, text='generate', fg='blue', height=5, width=10, command=sample_eq)
btn_generate.place(x=380, y=200)

gui.mainloop()
