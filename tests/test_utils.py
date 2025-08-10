from contextlib import nullcontext as does_not_raise
import pytest
import utilities.utils as utils
import os


Expectation = pytest.RaisesExc | does_not_raise


@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ("This is a test String", ["this", "is", "a", "string"]),
        ("This is a test String?", ["this", "is", "a", "string"]),
        ("", None),
        ("?.,;:!", None),
        ("1234", ["1234"]),
        (1234, ["1234"]),
        ("My name is O'Brien", ["my", "name", "is", "o'brien"]),
        ("\n", None),
    ]
)
def test_sanitize_query(input: str, expected: list[str]):
    """Checks that the value passed in can be stripped of special characters and split atomically

    .. test::
        :id: TTC012
        :tests: REQ012
    """
    result = utils.sanitize_query(input)
    assert result == expected

@pytest.mark.parametrize(
    ('input'),
    [
        ("file.txt"),
        (""),
    ]
)
def test_get_absolute_path(input: str) -> str:
    """Checks that the filepath passed incan be converted to an absolute file path

    .. test::
        :id: TTC013
        :tests: REQ001
    """
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    result = ROOT_DIR.replace('utilities', input)
    assert result == utils.get_absolute_path(input)