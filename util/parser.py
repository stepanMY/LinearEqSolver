import numpy as np
import re
import string


class WrongInputError(Exception):
    pass


def delete_spaces(string_val):
    """
    Delete spaces/tabs/newlines from string

    @param string_val: string, string to clear
    """
    cleared = re.sub(r"[\n\t\s]*", "", string_val)
    return cleared


class EqParser:
    """
    Class that parses linear equations from string
    """

    def __init__(self, variables=None):
        """
        @param variables: set, literals that are used as variable names
        if None, use lowercase latin letters
        """
        if variables is None:
            self.variable_names = set(string.ascii_lowercase)
        else:
            self.variable_names = variables

    def parse_eq(self, eq):
        """
        Parse equation
        return dictionary with coefficients and answer

        @param eq: string, equation to parse
        """
        result = dict()
        a_part, b_part = eq.split("=")
        result['answer'] = float(b_part)
        stack = ''
        for i in range(len(a_part)):
            elem = a_part[i]
            if elem in self.variable_names:
                if elem not in result:
                    if stack == '':
                        result[elem] = 1.0
                    elif stack == '+':
                        result[elem] = 1.0
                    elif stack == '-':
                        result[elem] = -1.0
                    else:
                        result[elem] = float(stack)
                    stack = ''
                else:
                    raise WrongInputError()
            else:
                stack += elem
        return result

    def parse_eqs(self, eqs):
        """
        Parse equations
        return np.arrays A and b

        @param eqs: string, equations to parse
        """
        eqs_clear = delete_spaces(eqs)
        eqs_parsed = [self.parse_eq(eq) for eq in eqs_clear.split(',')]
        variables = set()
        for row in eqs_parsed:
            for elem in row:
                if elem == 'answer':
                    continue
                variables.add(elem)
        variable_to_id = dict()
        variables_list = sorted(list(variables))
        for i in range(len(variables_list)):
            variable_to_id[variables_list[i]] = i
        a = np.zeros((len(eqs_parsed), len(variables_list)))
        b = np.zeros(len(eqs_parsed))
        for i in range(len(eqs_parsed)):
            row = eqs_parsed[i]
            for key in row:
                if key == 'answer':
                    b[i] = row[key]
                else:
                    a[i][variable_to_id[key]] = row[key]
        return a, b
