# -*- coding: utf-8 -*-
"""pyahp.methods.geometric

This module contains the class implementing the geometric priority estimation method.
"""

import numpy as np

from pyahp.methods import Method


class GeometricMethod(Method):
    """Geometric priority estimation method
    """

    def estimate(self, preference_matrix):
        super()._check_matrix(preference_matrix)
        height = preference_matrix.shape[1]
        return np.prod(preference_matrix, axis=1) ** (1/height)
