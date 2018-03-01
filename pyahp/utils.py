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
        crit_pr (list(float)): The priorities of all criteria.

    Returns:
       Normalized priorities
    """
    crit_attr_pr = [criterion.get_priorities() for criterion in criteria]
    attr_global_pr = [list(crit_pr[i]* crit_attr_pr[i]) for i in range(len(crit_pr))]

    return np.sum(np.transpose(attr_global_pr), axis=1)
