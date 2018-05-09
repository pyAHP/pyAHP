# -*- coding: utf-8 -*-
"""pyahp.hierarchy.ahpcriterion

This module contains the class definition for the AHP Criteria Node in the hierarchy model.
"""

import numpy as np

from pyahp.methods import EigenvalueMethod
from pyahp.utils import normalize_priorities, to_reciprocal_matrix


class AHPCriterion:
    """AHPCriterion

    Args:
        name (str): Name of the criterion this node resembles.
        model (dict): The Analytic Hierarchy Process model.
        solver (pyahp.methods): Method used when calculating the priorities of the lower layer.
    """

    def __init__(self, name, model, solver=EigenvalueMethod):
        self.name = name
        self.solver = solver()
        self.preference_matrices = model['preferenceMatrices']
        self.leaf = False

        sub_criteria = model['subCriteria'].get(name)

        if sub_criteria is not None:
            self.sub_criteria = [AHPCriterion(n, model, solver) for n in sub_criteria]
            self.p_m_key = 'subCriteria:{}'.format(name)
        else:
            self.leaf = True
            self.p_m_key = 'alternatives:{}'.format(name)

    def __str__(self):
        return self.name

    def get_priorities(self):
        """Get the priority of the nodes in the level below this node.

        Returns:
            Priorities at current level, normalized if an internal node.
        """
        p_m = np.array(self.preference_matrices[self.p_m_key])
        p_m = to_reciprocal_matrix(p_m)
        sub_crit_pr = self.solver.estimate(p_m)

        if self.leaf:
            return sub_crit_pr

        criteria_pr = [criterion.get_priorities() for criterion in self.sub_criteria]

        return normalize_priorities(criteria_pr, sub_crit_pr)
