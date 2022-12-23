import pytest

from TauTestProject.stuff.accumulation import Accumulator

# -----------------------------
# Unit tests
# -----------------------------


def test_accummulator_init():
    accum = Accumulator()
    assert accum.count == 0


def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_count_cannot_assign_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute 'count'"):
        accum.count = 5

