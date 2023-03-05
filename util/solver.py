import numpy as np


class WrongSystemError(Exception):
    pass


def check_existence(a, b):
    """
    Check existence of solution using Kronecker–Capelli theorem

    @param a: np.array, matrix of coefficients
    @param b: np.array, array of constant terms
    """
    rank_a = np.linalg.matrix_rank(a)
    ab = np.hstack((a, b.reshape(-1, 1)))
    rank_ab = np.linalg.matrix_rank(ab)
    if rank_a == rank_ab:
        return True
    return False


def check_uniqueness(a):
    """
    Check uniqueness of solution

    @param a: np.array, matrix of coefficients
    """
    rank_a = np.linalg.matrix_rank(a)
    if rank_a == a.shape[1]:
        return True
    return False


class LinEqSolver:
    """
    Class that solves linear equations
    """

    def __init__(self, run_checks=True):
        """
        @param run_checks: bool, whether to run checks or not
        """
        self.run_checks = run_checks

    def solve(self, a, b):
        """
        Solve system of linear equations
        return number of solutions and solutions themselves
        number of solutions are strings in {'none','inf','only'}
        solutions are numpy array

        @param a: np.array, matrix of coefficients
        @param b: np.array, array of constant terms
        """
        if self.run_checks:
            if not check_existence(a, b):
                return 'none', None
            if not check_uniqueness(a):
                return 'inf', None
        if a.shape[0] != a.shape[1]:
            # !!probably incorrect!!
            sol = np.linalg.pinv(a) @ b
            # !!probably incorrect!!
            return 'only', sol
        sol = np.linalg.solve(a, b)
        return 'only', sol
