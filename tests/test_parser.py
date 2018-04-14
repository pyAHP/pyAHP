import pytest

from pyahp import parse
from pyahp.errors import *


def test_empty_model():
    model = {}

    with pytest.raises(AHPModelError):
        parse(model)


def test_non_dict_model():
    model = []

    with pytest.raises(AHPTypeMismatchError):
        parse(model)


def test_model_with_missing_method():
    model = {
        'criteria': ['A', 'B'],
        'subCriteria': {},
        'alternatives': ['D', 'E', 'F'],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'alternatives:A': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPFieldEmptyError):
        parse(model)


def test_model_with_non_string_method():
    model = {
        'method': ['eigenvalue'],
        'criteria': ['A', 'B'],
        'subCriteria': {},
        'alternatives': ['D', 'E', 'F'],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'alternatives:A': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPTypeMismatchError):
        parse(model)


def test_model_with_unsupported_method():
    model = {
        'method': 'ahp',
        'criteria': ['A', 'B'],
        'subCriteria': {},
        'alternatives': ['D', 'E', 'F'],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'alternatives:A': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPMethodUnsupportedError):
        parse(model)


def test_model_with_non_string_criteria():
    model = {
        'method': 'geometric',
        'criteria': [1, 2],
        'subCriteria': {},
        'alternatives': ['D', 'E', 'F'],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'alternatives:1': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:2': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPTypeMismatchError):
        parse(model)


def test_model_with_missing_criteria_pm():
    model = {
        'method': 'geometric',
        'criteria': ['A', 'B'],
        'subCriteria': {},
        'alternatives': ['C', 'D', 'E'],
        'preferenceMatrices': {
            'alternatives:A': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPMissingPreferenceMatrixError):
        parse(model)


def test_model_with_non_string_alternatives():
    model = {
        'method': 'geometric',
        'criteria': ['A', 'B'],
        'subCriteria': {},
        'alternatives': [1, 2, 3],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'alternatives:A': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPTypeMismatchError):
        parse(model)
