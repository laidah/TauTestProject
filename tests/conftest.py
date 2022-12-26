import pytest

from TauTestProject.stuff.accumulation import Accumulator


@pytest.fixture
def accum():
    return Accumulator()