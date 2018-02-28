import numpy as np

from pyahp.hierarchy import AHPCriteria
from pyahp.methods import EigenvalueMethod


class AHPRoot:
    def __init__(self, config, solver=EigenvalueMethod):
        self.config = config
        self.solver = solver()

        criteria = config.get('criteria')

        if criteria is not None:
            self.criteria = [AHPCriteria(n, config, solver=solver) for n in criteria]
        else:
            raise ValueError('Empty list of criteria')

    def get_priorities(self):
        crit_pm = np.array(self.config['preferenceMatrices']['criteria'])
        crit_pr = self.solver.estimate(crit_pm)

        crit_attr_pr = [criterion.get_priorities() for criterion in self.criteria]
        attr_global_pr = np.around([list(crit_pr[i]* crit_attr_pr[i]) for i in range(len(crit_pr))], decimals=3)

        priorities = np.sum(np.transpose(attr_global_pr), axis=1)

        return priorities, attr_global_pr
