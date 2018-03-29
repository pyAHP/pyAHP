import numpy as np

from pyahp.utils import normalize_priorities


def test_normalize_priorities_1():
    criteria_pr = np.array([[1.0], [2.0], [3.0]])
    global_pr = np.array([1.0, 2.0, 3.0])

    result = normalize_priorities(criteria_pr, global_pr)
    expected = np.array([14.0])

    assert np.array_equal(expected, result)


def test_normalize_priorities_2():
    criteria_pr = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
    global_pr = np.array([1.0, 2.0, 3.0])

    result = normalize_priorities(criteria_pr, global_pr)
    expected = np.array([6.0, 12.0, 18.0])

    assert np.array_equal(expected, result)
