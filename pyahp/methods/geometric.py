from pyahp.methods import Method

import numpy as np


class GeometricMethod(Method):
    def estimate(self, preference_matrix):
        super()._check_matrix(preference_matrix)

        return np.array([np.prod(row)**(1/len(row)) for row in preference_matrix])
