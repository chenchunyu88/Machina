from machina.src.core import compute_cost

import pytest


def test_compute_cost():
    res = compute_cost(0.0, 750.0, 0.1, 3125.0, 0.0, 0, 1, 2)

    assert res[0] == 100
