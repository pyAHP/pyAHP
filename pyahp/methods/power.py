# -*- coding: utf-8 -*-
"""pyahp.methods.approximate

This module contains the class implementing the geometric priority estimation method.
"""

import numpy as np
import numpy.linalg as LA

from pyahp.methods import Method


def eig(A, initvec=None, tol=0.0001, iteration=15):
    '''Calculate the dominant eigenvalue of A with power method.

    The Power Method is a classical method to calculate the single eigenvalue with maximal abstract value, 
    i.e. |lambda_1| > |lambda2| >= |lambda_i|, where lambdai are eigenvalues, in numerical analysis.
    The speed of convergence is dominated by |lambda2|/|lambda1|.

    Perron theorem guarantees that lambda_1>|lambda_i| for any positive matrix.
    see https://en.wikipedia.org/wiki/Power_iteration for more details.
    
    Arguments:
        A {2D-array} -- square matrix
    
    Keyword Arguments:
        initvec {1D-array} -- [initial vector] (default: {None})
        tol {number} -- [tolerance] (default: {0.0001})
        iteration {number} -- [iteration] (default: {10})
    
    Returns:
        dominant eigenvalue, eigenvector {1D-array}

    Example:
    >>> A = np.array([[1,2,6],[1/2,1,4],[1/6,1/4,1]])
    >>> lmd, v = eig(A)
    >>> lmd
    3.0090068360243256
    >>> v
    [1.         0.5503254  0.15142866]
    '''

    m, n = A.shape
    u0 = initvec or np.random.random(n)
    for _ in range(iteration):
        v0 = u0
        v1 = np.dot(A, v0)
        ind = np.argmax(abs(v1))
        mu = v1[ind]
        u0 = v1 / mu
        if LA.norm(v0 - u0)/np.max((1, LA.norm(u0))) < tol:
            return mu, u0
    raise Exception('The iteration does not reach the tolerance after %d iterations.'%iteration)


class PowerMethod(Method):
    """Power priority estimation method
    """

    def estimate(self, preference_matrix):
        super()._check_matrix(preference_matrix)

        _, vec = eig(preference_matrix)

        return vec / np.sum(vec)
