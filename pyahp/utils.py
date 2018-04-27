# -*- coding: utf-8 -*-
"""pyahp.utils

This module contains the common functions and methods used by other modules in the class.
"""

import numpy as np


def normalize_priorities(criteria_pr, global_pr):
    """Normalize the priorities received from the lower layer.

    This function performs a Global Prioritization at the current node.

    Args:
        criteria_pr (list(list(float))): The priorities of all the alternatives/sub-criteria.
        global_pr (list(float)): The global priorities of all criteria.

    Returns:
       Normalized priorities
    """
    
    return np.dot(global_pr, criteria_pr)


def to_reciprocal_matrix(A):
    '''translate A to a reciprocal matrix
    
    If A is not a reciprocal matrix, pls translate A to a reciprocal matrix by this function.
    
    Arguments:
        A {2Darray|list(list)} -- The preference matrix
    
    Returns:
        2Darray|list(list) -- Reciprocal matrix
    '''

    A = A.astype(np.float64)
    m, n = A.shape
    for i in range(m):
        for j in range(n):
            if j == i:
                A[i, i] = 1
            elif A[i, j]==0:
                if A[j, i] !=0:
                    A[i, j] = 1/A[j, i]
                else:
                    for k in range(m):
                        if A[i, k] !=0 and A[k, j] !=0:
                            A[i, j] = A[i, k] * A[k, j]
                            break
                    else:
                        raise ValueError('There are so many zeros! I am not able to convert A[%d,%d] to a vaild value!'%(i,j))
    return A


def is_reciprocal(A):
    # return True if A is a reciprocal matrix
    m, n = A.shape
    for i in range(m):
        for j in range(i):
            if A[i, j] * A[j,i] != 1:
                return False
    return True

def is_positive_reciprocal(A):
    # return True if A is a reciprocal matrix
    m, n = A.shape
    for i in range(m):
        if A[i, i] != 1:
            return False
        for j in range(i):
            if A[i,j]>0 and A[i, j] * A[j,i] != 1:
                return False
    return True
