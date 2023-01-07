import pytest
from stuff.accumulation import Accumulator


@pytest.fixture
def accum():
    return Accumulator()