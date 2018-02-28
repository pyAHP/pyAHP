import numpy as np

from pyahp.methods import Method


class ApproximateMethod(Method):
    def estimate(self, preference_matrix):
        super()._check_matrix(preference_matrix)

        row_sums = np.sum(preference_matrix, axis=1)
        total_sum = np.sum(row_sums)

        return np.array([(row_sum/total_sum) for row_sum in row_sums])
