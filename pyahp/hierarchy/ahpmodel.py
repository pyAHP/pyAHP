# -*- coding: utf-8 -*-
"""pyahp.hierarchy.ahpmodel

This module contains the class definition for the AHP Model Node (root) in the hierarchy model.
"""

import numpy as np

from pyahp.hierarchy import AHPCriterion
from pyahp.methods import EigenvalueMethod
from pyahp.utils import normalize_priorities


class AHPModel:
    """AHPModel

    Args:
        model (dict): The Analytic Hierarchy Process model.
        solver (pyahp.methods): Method used when calculating the priorities of the lower layer.
    """

    def __init__(self, model, solver=EigenvalueMethod):
        self.solver = solver()
        self.preference_matrices = model['preferenceMatrices']

        criteria = model.get('criteria')
        self.criteria = [AHPCriterion(n, model, solver=solver) for n in criteria]

    def get_priorities(self, round_results=True, decimals=3):
        """Get the priority of the nodes in the level below this node.

        Args:
            round_results (bool): Return rounded priorities. Default is True.
            decimals (int): Number of decimals to round to, ignored if `round_results=False`. Default is 3.

        Returns:
            Global priorities of the alternatives in the model, rounded to `decimals` positions if `round_results=True`.
        """
        crit_pm = np.array(self.preference_matrices['criteria'])
        crit_pr = self.solver.estimate(crit_pm)

        priorities = normalize_priorities(self.criteria, crit_pr)

        if round_results:
            return np.around(priorities, decimals=decimals)

        return priorities
