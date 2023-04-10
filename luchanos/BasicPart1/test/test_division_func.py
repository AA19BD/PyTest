import pytest

from PyTest.luchanos.BasicPart1.utils import division


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (10, 5, 2),
                                                   (10, 1, 10),
                                                   (10, -5, -2),
                                                   (10, -2, -5)])
def test_division_one_more(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, divider, div", [(ZeroDivisionError, 0, 10), (TypeError, '2', 10)])
def test_division_error(expected_exception, divider, div):
    with pytest.raises(expected_exception):
        division(div, divider)
