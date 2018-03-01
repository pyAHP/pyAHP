# -*- coding: utf-8 -*-
"""pyahp.methods.eigenvalue

This module contains the class implementing the eigenvalue priority estimation method.
"""

import numpy as np
from scipy.sparse.linalg import eigs

from pyahp.methods import Method


RANDOM_INDICES = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51]


class EigenvalueMethod(Method):
    """Eigenvalue based priority estimation method
    """

    @staticmethod
    def _evaluate_consistency(matrix):
        width = matrix.shape[0]

        if width > len(RANDOM_INDICES):
            return 0

        return RANDOM_INDICES[width - 1]

    def estimate(self, preference_matrix):
        super()._check_matrix(preference_matrix)
        width = preference_matrix.shape[0]

        _, vectors = eigs(preference_matrix, k=(width-2), sigma=width, which='LM', v0=np.ones(width))

        real_vector = np.real([vec for vec in np.transpose(vectors) if not np.all(np.imag(vec))][:1])
        sum_vector = np.sum(real_vector)

        self._evaluate_consistency(preference_matrix)

        return np.around([v / sum_vector for v in real_vector], decimals=3)[0]
