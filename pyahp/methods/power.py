# -*- coding: utf-8 -*-
"""pyahp.methods.approximate

This module contains the class implementing the geometric priority estimation method.
"""

import numpy as np
import numpy.linalg as LA

from pyahp.methods import Method


def eig(A, initvec=None, tol=0.0001, iteration=10):
    '''calculate the max eigenvalue of A
    
    Arguments:
        A {2D-array} -- square matrix
    
    Keyword Arguments:
        initvec {1D-array} -- [initial vector] (default: {None})
        tol {number} -- [tolerance] (default: {0.0001})
        iteration {number} -- [iteration] (default: {10})
    
    Returns:
        eigenvalue, eigenvector
    '''

    m, n = A.shape
    u0 = initvec or np.ones(n)
    k = 0
    while True:
        v0 = u0
        v1 = np.dot(A, v0)
        ind = np.argmax(abs(v1))
        mu = v1[ind]
        u0 = v1 / mu
        k += 1
        if k >= iteration or LA.norm(v0 - u0)/np.max((1, LA.norm(u0))) < tol:
            return mu + n, u0


class PowerMethod(Method):
    """Power priority estimation method
    """

    def estimate(self, preference_matrix):
        super()._check_matrix(preference_matrix)

        _, vec = eig(preference_matrix)

        return vec / np.sum(vec)
