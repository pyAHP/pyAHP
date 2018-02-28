import numpy as np

from pyahp.methods import EigenvalueMethod


class AHPCriteria:
    def __init__(self, name, config, solver=EigenvalueMethod):
        self.name = name
        self.config = config
        self.solver = solver()
        self.leaf = False

        sub_criteria = config['subCriteria'].get(name)

        if sub_criteria is not None:
            self.sub_criteria = [AHPCriteria(n, config) for n in sub_criteria]
        else:
            self.leaf = True

    def get_priorities(self):
        if self.leaf:
            pm_str = f'alternatives:{self.name}'
        else:
            pm_str = f'subCriteria:{self.name}'

        pm = np.array(self.config['preferenceMatrices'][pm_str])
        return self.solver.estimate(pm)
