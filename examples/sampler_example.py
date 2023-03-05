from randomizer.sampler import EqSampler

sampler = EqSampler(12)
n_equations = [5, 6, 7]
coefficients = [-1, 1, 0.5]
n_variables = [6, 7]
answers = [1, 2, 3, 4, 5, 6, 7]
print(sampler.generate_equations(n_equations, coefficients, n_variables, answers))
