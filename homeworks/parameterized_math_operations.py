import pytest
from pytest import approx


sum_data = [("3+5", 8), ("3+8", 11), ("30+8", 38)]
subtract_data = [("3-5", -2), ("3-8", -5), ("30-8", 22)]
multiply_data = [("3*5", 15), ("3*8", 24), ("30*8", 240)]
divide_data = [("3/5", 0.6), ("3/4", 0.75), ("30/8", 3.75)]


@pytest.mark.parametrize("test_input,expected", sum_data)
@pytest.mark.usefixtures('before_function_sum')
@pytest.mark.usefixtures('before_class')
def test_sum(test_input, expected):
    assert eval(test_input) == expected
    print('\nSum passed')


@pytest.mark.parametrize("test_input,expected", subtract_data)
@pytest.mark.usefixtures('before_function_subtraction')
@pytest.mark.usefixtures('before_class')
def test_subtract(test_input, expected):
    assert eval(test_input) == expected
    print('\nSubtraction passed')


@pytest.mark.parametrize("test_input,expected", multiply_data)
@pytest.mark.usefixtures('before_function_multiplying')
@pytest.mark.usefixtures('before_class')
def test_multiply(test_input, expected):
    assert eval(test_input) == expected
    print('\nMultiplying passed')


@pytest.mark.parametrize("test_input,expected", divide_data)
@pytest.mark.usefixtures('before_function_division')
@pytest.mark.usefixtures('before_class')
def test_divide(test_input, expected):
    assert eval(test_input) == expected
    print('\nDividing passed')
