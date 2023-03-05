import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from util.parser import EqParser
from util.solver import LinEqSolver


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
    Solve system of linear equations and print result
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


parser = EqParser()
solver = LinEqSolver()
gui = tk.Tk()
gui.geometry('800x400')

eqs_fld = ScrolledText(gui, height=10, width=30)
eqs_fld.place(x=80, y=150)

res_fld = ScrolledText(gui, height=10, width=30, state='disabled')
res_fld.place(x=500, y=150)

btn = tk.Button(gui, text='solve', fg='blue', height=5, width=5, command=solve_eq)
btn.place(x=80+300, y=100)

gui.mainloop()
