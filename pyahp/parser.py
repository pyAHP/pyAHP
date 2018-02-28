import numpy as np
from queue import Queue

from pyahp.errors import AHPConfigError
from pyahp.hierarchy import AHPRoot
from pyahp.methods import ApproximateMethod, EigenvalueMethod, GeometricMethod


def _type(val):
    return val.__class__.__name__


def _check_ahp_list(name, value):
    if not isinstance(value, list):
        raise AHPConfigError('Expecting {} to be a list got {}'.format(name, _type(value)))

    for v in value:
        if not isinstance(v, str):
            raise AHPConfigError('Expecting {} list to have string got {}'.format(name, _type(v)))

    if len(value) != len(set(value)):
        raise AHPConfigError('{} list contains duplicates'.format(name))


def _check_ahp_preference_matrix(name, p_m, kind, length):
    if p_m is None:
        raise AHPConfigError('Missing {} preference matrix for {}'.format(kind, name))

    p_m = np.array(p_m)

    width, height = p_m.shape
    if width != height or width != length:
        raise AHPConfigError(
            'Expecting {0}:{1} preference matrix to be {2}x{2} got {3}x{4}'.format(kind,
                                                                                   name,
                                                                                   length,
                                                                                   width,
                                                                                   height)
        )


def validate_config(config):
    if not isinstance(config, dict):
        raise AHPConfigError('Expecting a config dictionary got {}'.format(_type(config)))

    method = config['method']
    if not isinstance(method, str):
        raise AHPConfigError('Expecting method to be string got {}'.format(_type(method)))

    if method not in ['approximate', 'eigenvalue', 'geometric']:
        raise AHPConfigError('Expecting method to be approximate, eigenvalue or geometric')

    _check_ahp_list('criteria', config['criteria'])
    _check_ahp_list('alternatives', config['alternatives'])

    n_alternatives = len(config['alternatives'])
    preference_matrices = config['preferenceMatrices']
    criteria = config['criteria']
    criteria_queue = Queue()

    criteria_p_m = preference_matrices.get('criteria')
    _check_ahp_preference_matrix(name='criteria',
                                 p_m=criteria_p_m,
                                 kind="criteria",
                                 length=len(criteria))

    for criterion in criteria:
        criteria_queue.put(criterion)

    sub_criteria_map = config.get('subCriteria')

    while not criteria_queue.empty():
        criterion = criteria_queue.get()
        sub_criteria = sub_criteria_map.get(criterion)

        if sub_criteria:
            _check_ahp_list('subCriteria:{}'.format(criterion), sub_criteria)

            p_m = preference_matrices.get('subCriteria:{}'.format(criterion))
            _check_ahp_preference_matrix(name=criterion,
                                         p_m=p_m,
                                         kind="subCriteria",
                                         length=len(sub_criteria))

            for sub_criterion in sub_criteria:
                criteria_queue.put(sub_criterion)
        else:
            p_m = preference_matrices.get('alternatives:{}'.format(criterion))
            _check_ahp_preference_matrix(name=criterion,
                                         p_m=p_m,
                                         kind="alternatives",
                                         length=n_alternatives)


def parse(config):
    validate_config(config)

    method = config['method']

    if method == 'approximate':
        solver = ApproximateMethod
    elif method == 'eigenvalue':
        solver = EigenvalueMethod
    elif method == 'geometric':
        solver = GeometricMethod

    return AHPRoot(config, solver)
