import pytest

from helper import is_even


@pytest.mark.parametrize("x,expected", [
    (0, True),
    (2, True),
    (-4, True),
    (1, False),
    (99, False),
])
def test_is_even_param(x, expected):
    """Parametrized tests for is_even."""
    assert is_even(x) is expected
