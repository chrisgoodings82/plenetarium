from contextlib import nullcontext as does_not_raise
import pytest
import utilities.long_responses as long
import random

Expectation = pytest.RaisesExc | does_not_raise


def test_unknown():
    """Checks that a random resonse can be generated

    .. test::
        :id: TTC003
        :tests: REQ003
    """
    sample_strings = ['response | Could you please re-phrase that?',
            'response | I\'m not quite sure what you mean...',
            'response | Hmmm, that is a tough one... could you try a different question, please?']
    
    # Act
    result = long.R_UNKNOWN[random.randrange(3)]
    
    # Assert
    assert result in sample_strings
        
def test_pluto():
    """Checks that an explaination for Pluto is provided

    .. test::
        :id: TTC004
        :tests: REQ011
    """
    # Act
    result = long.R_PLUTO

    # Assert
    assert result == "Pluto, once considered the ninth planet, is now classified as a dwarf planet. It is located in the Kuiper Belt, a region beyond Neptune, and is known for its icy surface and five moons, the largest being Charon."
    