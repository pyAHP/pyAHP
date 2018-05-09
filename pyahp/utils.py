# -*- coding: utf-8 -*-
"""pyahp.utils

This module contains the common functions and methods used by other modules in the class.
"""

import numpy as np

from pyahp.errors import AHPPreferenceMatrixConversionError


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
        A[i, i] = 1
        for j in range(n):
            if j == i or A[i, j] != 0: #filter this case
                continue
            if A[j, i] !=0:
                A[i, j] = 1/A[j, i]
            else:
                A[i, j] = np.mean([A[i, k] * A[k, j] for k in range(m) if A[i, k] !=0 and A[k, j] !=0])
                if A[i, j] != 0:
                    A[j, i] = 1/A[i, j]
                else:
                    raise AHPPreferenceMatrixConversionError(pm=A, loc=(i, j))
    return A
