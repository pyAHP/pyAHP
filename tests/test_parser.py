import pytest

from pyahp import parse
from pyahp.errors import *


def test_empty_model():
    model = {}

    with pytest.raises(AHPModelError):
        parse(model)


def test_non_dict_model():
    model = []

    with pytest.raises(AHPTypeMismatchError) as err:
        parse(model)

    assert err.value.var == 'model'
    assert err.value.expected == 'dict'
    assert err.value.actual == 'list'


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

    with pytest.raises(AHPFieldEmptyError) as err:
        parse(model)

    assert err.value.var == 'method'


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

    with pytest.raises(AHPTypeMismatchError) as err:
        parse(model)

    assert err.value.var == 'method'
    assert err.value.expected == 'str'
    assert err.value.actual == 'list'


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

    with pytest.raises(AHPMethodUnsupportedError) as err:
        parse(model)

    assert err.value.actual == 'ahp'


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

    with pytest.raises(AHPTypeMismatchError) as err:
        parse(model)

    assert err.value.var == 'criteria'
    assert err.value.expected == 'str'
    assert err.value.actual == 'int'


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

    with pytest.raises(AHPMissingPreferenceMatrixError) as err:
        parse(model)

    assert err.value.kind == 'criteria'
    assert err.value.name == 'criteria'


def test_model_with_non_square_criteria_pm():
    model = {
        'method': 'geometric',
        'criteria': ['A', 'B'],
        'subCriteria': {},
        'alternatives': ['C', 'D', 'E'],
        'preferenceMatrices': {
            'criteria': [[1, 2, 0], [0.5, 1, 0]],
            'alternatives:A': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPNonSquarePreferenceMatrixError) as err:
        parse(model)

    assert err.value.kind == 'criteria'
    assert err.value.name == 'criteria'
    assert err.value.side == 2
    assert err.value.actual_width == 2
    assert err.value.actual_height == 3


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

    with pytest.raises(AHPTypeMismatchError) as err:
        parse(model)

    assert err.value.var == 'alternatives'
    assert err.value.expected == 'str'
    assert err.value.actual == 'int'


def test_model_with_missing_alternative_pm():
    model = {
        'method': 'geometric',
        'criteria': ['A', 'B'],
        'subCriteria': {},
        'alternatives': ['C', 'D', 'E'],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'alternatives:A': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        }
    }

    with pytest.raises(AHPMissingPreferenceMatrixError) as err:
        parse(model)

    assert err.value.kind == 'alternatives'
    assert err.value.name == 'B'


def test_model_with_non_square_alternative_pm():
    model = {
        'method': 'geometric',
        'criteria': ['A', 'B'],
        'subCriteria': {},
        'alternatives': ['C', 'D', 'E'],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'alternatives:A': [[1, 1], [1, 1], [1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPNonSquarePreferenceMatrixError) as err:
        parse(model)

    assert err.value.kind == 'alternatives'
    assert err.value.name == 'A'
    assert err.value.side == 3
    assert err.value.actual_width == 3
    assert err.value.actual_height == 2


def test_model_with_non_string_sub_criteria():
    model = {
        'method': 'geometric',
        'criteria': ['A', 'B'],
        'subCriteria': {
            'A': ['A1', 2]
        },
        'alternatives': ['C', 'D', 'E'],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'alternatives:A': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPTypeMismatchError) as err:
        parse(model)

    assert err.value.var == 'subCriteria:A'
    assert err.value.expected == 'str'
    assert err.value.actual == 'int'


def test_model_without_sub_criteria_pm():
    model = {
        'method': 'geometric',
        'criteria': ['A', 'B'],
        'subCriteria': {
            'A': ['A1', 'A2']
        },
        'alternatives': ['C', 'D', 'E'],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'alternatives:A1': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:A2': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPMissingPreferenceMatrixError) as err:
        parse(model)

    assert err.value.kind == 'subCriteria'
    assert err.value.name == 'A'


def test_model_without_sub_criteria_alternative_pm():
    model = {
        'method': 'geometric',
        'criteria': ['A', 'B'],
        'subCriteria': {
            'A': ['A1', 'A2']
        },
        'alternatives': ['C', 'D', 'E'],
        'preferenceMatrices': {
            'criteria': [[1, 2], [0.5, 1]],
            'subCriteria:A': [[1, 1], [1, 1]],
            'alternatives:A1': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'alternatives:B': [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        }
    }

    with pytest.raises(AHPMissingPreferenceMatrixError) as err:
        parse(model)

    assert err.value.kind == 'alternatives'
    assert err.value.name == 'A2'
