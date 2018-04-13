# -*- coding: utf-8 -*-
"""pyahp.parser

This module contains the functions required to perform AHP Model validation.
"""

from queue import Queue
import numpy as np

from pyahp.errors import AHPModelError
from pyahp.hierarchy import AHPModel
from pyahp.methods import ApproximateMethod, EigenvalueMethod, GeometricMethod


def _type(val):
    return val.__class__.__name__


def _check_ahp_list(name, value):
    if not isinstance(value, list):
        raise AHPModelError('Expecting {} to be a list got {}'.format(name, _type(value)))

    if not value:
        raise AHPModelError('{} list empty'.format(name))

    for elem in value:
        if not isinstance(elem, str):
            raise AHPModelError('Expecting {} list to have string got {}'.format(name, _type(elem)))

    if len(value) != len(set(value)):
        raise AHPModelError('{} list contains duplicates'.format(name))


def _check_ahp_preference_matrix(name, p_m, kind, length):
    if p_m is None:
        raise AHPModelError('Missing {} preference matrix for {}'.format(kind, name))

    p_m = np.array(p_m)

    width, height = p_m.shape
    if width != height or width != length:
        raise AHPModelError(
            'Expecting {0}:{1} preference matrix to be {2}x{2} got {3}x{4}'.format(kind,
                                                                                   name,
                                                                                   length,
                                                                                   width,
                                                                                   height)
        )

methods = ('approximate', 'eigenvalue', 'geometric', 'power')
def validate_model(model):
    """Validate the passed AHP model.

    Args:
        model (dict): The Analytic Hierarchy Process model.

    Raises:
        AHPModelError when the model validation fails.
    """

    if not isinstance(model, dict):
        raise AHPModelError('Expecting a config dictionary got {}'.format(_type(model)))

    method = model['method']
    if not isinstance(method, str):
        raise AHPModelError('Expecting method to be string got {}'.format(_type(method)))

    if method not in methods:
        raise AHPModelError('Expecting method to be one of %s'%(', '.join(methods)))

    _check_ahp_list('criteria', model['criteria'])
    _check_ahp_list('alternatives', model['alternatives'])

    n_alternatives = len(model['alternatives'])
    preference_matrices = model['preferenceMatrices']
    criteria = model['criteria']
    criteria_queue = Queue()

    criteria_p_m = preference_matrices.get('criteria')
    _check_ahp_preference_matrix(name='criteria',
                                 p_m=criteria_p_m,
                                 kind="criteria",
                                 length=len(criteria))

    for criterion in criteria:
        criteria_queue.put(criterion)

    sub_criteria_map = model.get('subCriteria')

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


def parse(model):
    """Parse the passed AHP model.

    Args:
        model (dict): The Analytic Hierarchy Process model.

    Returns:
        AHPModel with the specified solver.
    """
    validate_model(model)

    method_name = model['method'].capitalize() + 'Method'
    solver = globals()[method_name]

    return AHPModel(model, solver)
