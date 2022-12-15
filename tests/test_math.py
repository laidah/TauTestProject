import pytest


# Simple math test
def test_one_plus_one():
    assert 1 + 1 == 2


# Test verifies an exception
def test_division_by_zero_exception():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert "division by zero" in str(e.value)


# Parametrized tests for multiplication
parameters = [
    (2, 3, 6),          # positives
    (1, 99, 99),        # identity
    (-1, 3, -3),        # positive and negative
    (-3, -3, 9),        # two negatives
    (2.5, 6.7, 16.75),  # floats
    (0, 99, 0)          # zero
]


@pytest.mark.parametrize('a, b, result', parameters)
def test_multiplication(a, b, result):
    assert a * b == result

