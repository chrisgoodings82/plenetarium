import pytest

pytest_plugins = ('sphinx.testing.fixtures',)

@pytest.fixture
def input_value():
    input = 8
    return input