import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from util.parser import EqParser, WrongInputError
from util.solver import LinEqSolver, WrongSystemError


def solve_eq():
    input_val = eqs_fld.get('1.0', 'end-1c')
    try:
        a, b, mapping = parser.parse_eqs(input_val)
        mapping_inv = {mapping[key]: key for key in mapping}
    except:
        raise WrongInputError('Input is incorrect')
    try:
        n_sol, sol = solver.solve(a, b)
    except:
        raise WrongSystemError('System is not specified correctly')
    res_fld.configure(state='normal')
    res_fld.delete('1.0', 'end-1c')
    res_fld.insert(tk.INSERT, sol)
    res_fld.configure(state='disabled')

    print(n_sol, sol, mapping_inv)


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
