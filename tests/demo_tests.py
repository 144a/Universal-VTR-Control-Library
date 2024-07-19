# tests/demo_tests.py

import pytest
from uvcl import test

def test_test():
    assert test(1, 2) == 3
    assert test(-1, 1) == 0
    assert test(0, 0) == 0