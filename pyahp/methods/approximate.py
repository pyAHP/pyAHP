# -*- coding: utf-8 -*-
"""pyahp.methods.approximate

This module contains the class implementing the geometric priority estimation method.
"""

import numpy as np

from pyahp.methods import Method


class ApproximateMethod(Method):
    """Approximate priority estimation method
    """

    def estimate(self, preference_matrix):
        super()._check_matrix(preference_matrix)

        row_sums = np.sum(preference_matrix, axis=1)
        total_sum = np.sum(row_sums)

        return row_sums / total_sum
