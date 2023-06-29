import pytest


@pytest.fixture(scope='module')
def before_class():
    print('\nStarting math operations')
    yield
    print('\nMath operations finished')


@pytest.fixture()
def before_function_sum():
    print('\nBefore every sum')
    yield
    print('After every sum')


@pytest.fixture()
def before_function_subtraction():
    print('\nBefore every subtraction')
    yield
    print('After every subtraction')


@pytest.fixture()
def before_function_multiplying():
    print('\nBefore every multiplying')
    yield
    print('After every multiplying')


@pytest.fixture()
def before_function_division():
    print('\nBefore every division')
    yield
    print('After every division')


