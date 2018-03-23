# -*- coding: utf-8 -*-
"""pyahp.utils

This module contains the common functions and methods used by other modules in the class.
"""

import numpy as np


def normalize_priorities(criteria, crit_pr):
    """Normalize the priorities received from the lower layer.

    This function performs a Global Prioritization at the current node.


    Args:
        criteria (list(AHPCriterion)): List of all criteria.
        crit_pr (list(float) | 1D-array): The priorities of all criteria.

    Returns:
       Normalized priorities (1D-array): crit_pr * matrix of priorities of criteria
    """
    crit_attr_pr = np.array([criterion.get_priorities() for criterion in criteria])
    return np.dot(crit_pr, crit_attr_pr)
