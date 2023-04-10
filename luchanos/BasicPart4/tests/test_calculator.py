import pytest

from PyTest.luchanos.BasicPart4.my_func.calculator import simple_calculator


@pytest.mark.parametrize("num1, num2, operation, answer", [(1, 1, "/", 1),
                                                           (1, 1, "*", 1),
                                                           (1, 1, "+", 2),
                                                           (1, 1, "-", 0)])
def test_simple_calculator(num1, num2, operation, answer):
    assert simple_calculator(num1, num2, operation) == answer
