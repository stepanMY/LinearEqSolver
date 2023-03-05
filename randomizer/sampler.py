import numpy as np
import string


class EqSampler:
    """
    Class that samples equations
    """

    def __init__(self, random_seed=42, variables=None):
        """
        @param random_seed: int, random seed that is used in generation
        @param variables: set, literals that are used as variable names
        if None, use lowercase latin letters
        """
        self.random_seed = random_seed
        np.random.seed(self.random_seed)
        if variables is None:
            self.variables = list(string.ascii_lowercase)
        else:
            self.variables = variables

    def generate_equations(self, n_equations, coefficients, n_variables, answers):
        """
        Generate list of string equations

        @param n_equations: list, list from which number of equations is sampled
        @param coefficients: list, list from which coefficients are sampled (with replace)
        @param n_variables: list, list from which n_variables in which equation is sampled
        @param answers: list, list from which answers are sampled
        """
        n_eqs = np.random.choice(n_equations, 1)[0]
        vars_used = self.variables[:max(n_variables)]
        result = []
        for _ in range(n_eqs):
            n_vars = np.random.choice(n_variables)
            vars_sampled = np.random.choice(vars_used, n_vars, replace=False)
            coefs_sampled = np.random.choice(coefficients, n_vars, replace=True)
            eq = ''
            for i in range(n_vars):
                var, coef = vars_sampled[i], coefs_sampled[i]
                if coef >= 0:
                    if eq == '':
                        if coef == 1:
                            eq += var
                        else:
                            eq += str(coef)+var
                    else:
                        if coef == 1:
                            eq += '+'+var
                        else:
                            eq += '+'+str(coef)+var
                else:
                    if coef == -1:
                        eq += '-'+var
                    else:
                        eq += str(coef)+var
            answer_sampled = np.random.choice(answers, 1)[0]
            eq += '='+str(answer_sampled)
            result.append(eq)
        return result







