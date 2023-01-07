import pytest
from hypothesis import given, strategies as st


# ----------------
# Simple math test
# ----------------
def test_one_plus_one():
    assert 1 + 1 == 2


# --------------------------
# Test verifies an exception
# --------------------------
def test_division_by_zero_exception():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert "division by zero" in str(e.value)


# -------------------------------------
# Parametrized tests for multiplication
# -------------------------------------
parameters = [
    (2, 3, 6),  # positives
    (1, 99, 99),  # identity
    (-1, 3, -3),  # positive and negative
    (-3, -3, 9),  # two negatives
    (2.5, 6.7, 16.75),  # floats
    (0, 99, 0)  # zero
]


@pytest.mark.parametrize('a, b, result', parameters)
def test_multiplication(a, b, result):
    assert a * b == result


# ----------------------------------------
# Parametrized tests reading data from csv
# ----------------------------------------
def get_data(csv_name):
    with open(csv_name) as csv_file:
        params = []
        for row in csv_file:
            params.append([int(value) for value in row.split(',')])
    return params


@pytest.mark.parametrize('a, b, result', get_data('tests/fixtures/multiply_test_data.csv'))
def test_multiplication_csv_params(a, b, result):
    assert a * b == result


# ----------------------------
# Parametrized with hypothesis
# ----------------------------
def multiplication(a, b):
    return a * b


@given(st.integers(), st.integers())
@pytest.mark.hypothesis
def test_multiplication_hypothesis(a, b):
    assert multiplication(a, b) == multiplication(b, a)


@given(st.floats(allow_nan=False, allow_subnormal=False, allow_infinity=False), st.floats(allow_nan=False,
                                                                                          allow_subnormal=False,
                                                                                          allow_infinity=False))
@pytest.mark.hypothesis
def test_multiplication_floats(a, b):
    print("a = {}, b={}".format(a, b))
    assert multiplication(a, b) == multiplication(b, a)
