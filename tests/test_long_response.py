from contextlib import nullcontext as does_not_raise
import pytest
import utilities.long_responses as long

Expectation = pytest.RaisesExc | does_not_raise


def test_unknown():
    """Checks that a random resonse can be generated

    .. test::
        :id: TTC001
        :tests: REQ001
    """
    sample_strings = ['response | Could you please re-phrase that?',
            'response | I\'m not quite sure what you mean...',
            'response | Hmmm, that is a tough one... could you try a different question, please?']
    
    # Act
    result = long.unknown()
    
    # Assert
    assert result in sample_strings
