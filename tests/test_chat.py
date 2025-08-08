from contextlib import nullcontext as does_not_raise
import pytest
import scripts.chat as chat
from utilities.long_responses import R_PLUTO

Expectation = pytest.RaisesExc | does_not_raise

chat_instance = chat.chat()

@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ("This is a test String", "This is a test String"),
        ("", ""),
        ("1234", "1234"),
        (1234, "1234"),
        ("Special!!!", "Special!!!"),
        ("\n", "\n"),
    ]
)
def test_get_user_input(input, expected):
    """Checks that the value stored in the user_ipnut member returns a string value

    .. test::
        :id: TTC003
        :tests: REQ001
    """
    chat_instance.user_input = input
    assert chat_instance.get_user_input() == expected

@pytest.mark.parametrize(
    ('input', 'expected'),
    (
        ("Tell me everything about all planets.", """The planet Mercury is positioned 58000000.0 km from the Sun. It has a mass of 3.3011e+23 kg, a radius of 2439.7 km. Mercury has 0 moons. 
        The planet Venus is positioned 108200000.0 km from the Sun. It has a mass of 4.8675e+24 kg, a radius of 6051.0 km. Venus has 0 moons. 
        The planet Earth is positioned 150200000.0 km from the Sun. It has a mass of 5.972e+24 kg, a radius of 6378.0 km. Earth has 1 moon. This is: Luna. 
        The planet Mars is positioned 227900000.0 km from the Sun. It has a mass of 6.4171e+23 kg, a radius of 3389.5 km. Mars has 2 moons. These are: Phobos, Deimos. 
        The planet Jupiter is positioned 778500000.0 km from the Sun. It has a mass of 1.8982e+27 kg, a radius of 69911.0 km. Jupiter has 97 moons. The notable ones are: Europa, Ganymede, Io, Callisto. 
        The planet Saturn is positioned 1434000000.0 km from the Sun. It has a mass of 5.6834e+26 kg, a radius of 58232.0 km. Saturn has 274 moons. The notable ones are: Titan, Rhea, Mimas, Enceladus. 
        The planet Uranus is positioned 2871000000.0 km from the Sun. It has a mass of 8.681e+25 kg, a radius of 25362.0 km. Uranus has 28 moons. The notable ones are: Ariel, Umbriel, Titania, Oberon. 
        The planet Neptune is positioned 4495000000.0 km from the Sun. It has a mass of 1.024e+26 kg, a radius of 24622.0 km. Neptune has 16 moons. The notable ones are: Triton, Proteus. """),
        ("How far from the sun is Mercury?", "The planet Mercury is 58000000.0 km from the Sun."),
        ("Tell me about the mass of Venus", "The planet Venus has a mass of 4.8675e+24 kg."),
        ("How many moons does Jupiter have.!£$", "The planet Jupiter has 97 moons."),
        ("What are the moons of saturn?", "The planet Saturn has the following moons: Titan, Rhea, Mimas, Enceladus."),
        ("What is the radius of neptune", "The planet Neptune has a radius of 24622.0 km."),
        ("Hi", "Hello!"),
        ("How are you doing?", "I\'m doing fine, and you?"),
        ("Bye!", "Goodbye!"), 
        ("Is Pluto a planet?", f"{R_PLUTO}"),
        ("What is the largest moon?", "That's no moon!!!"),
        ("What are teh phases of teh moon?", "Full moon, Half moon, New moon...")
    )
)
def test_get_response(input, expected):
    """Checks that a random resonse can be generated

    .. test::
        :id: TTC001
        :tests: REQ003
    """
    result = chat_instance.get_response(input)
    assert result == expected