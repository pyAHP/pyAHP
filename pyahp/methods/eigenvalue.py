import numpy as np
from scipy.sparse.linalg import eigs

from pyahp.methods import Method


random_indices = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51]


class EigenvalueMethod(Method):

    @staticmethod
    def _evaluate_consistency(matrix):
        n, _ = matrix.shape

        if n > len(random_indices):
            return 0
        else:
            return random_indices[n - 1]

    def estimate(self, preference_matrix):
        super()._check_matrix(preference_matrix)
        n = preference_matrix.shape[0]

        v = np.ones(n)
        _, vectors = eigs(preference_matrix, k=(n-2), sigma=n, which='LM', v0=v)

        real_vector = np.real([v for v in np.transpose(vectors) if not np.all(np.imag(v))][:1])
        sum_vector = np.sum(real_vector)

        # TODO: Check result consistency

        return np.around([v / sum_vector for v in real_vector], decimals=3)[0]
