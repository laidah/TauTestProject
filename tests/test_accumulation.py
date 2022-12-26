import pytest

# -----------------------------
# Unit tests
# -----------------------------


def test_accummulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_count_cannot_assign_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute 'count'"):
        accum.count = 5

