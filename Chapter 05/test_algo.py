# pytest expects the test file name to be in the format: ‘*_test.py’ or ‘test_*.py’

import algo


def test_min():
    """Verify the output of the 'min' function"""
    values = [2, 5, 6, 1, 8]
    assert algo.minimum(values) == 1


def test_max():
    """Verify the output of the 'max' function"""
    values = [2, 5, 6, 1, 9, 4, 9]
    assert algo.maximum(values) == 9


def test_total():
    """Verify the output of the 'total' function"""
    values = [5, 6, 7]
    assert algo.total(values) == 18


def test_is_empty():
    """Verify the output of the 'is_empty' function"""
    values = [1, 2]
    assert algo.is_empty(values) == False
