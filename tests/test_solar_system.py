from contextlib import nullcontext as does_not_raise
import pytest
import scripts.solar_system as ss
import scripts.planet as planet


Expectation = pytest.RaisesExc | does_not_raise

solar_system_instance = ss.solar_system()
solar_system_instance.init_solar_system()

@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ("mass", {"mercury": 3.3011e23, "venus": 4.8675e24, "earth": 5.972e24, "mars": 6.4171e23, "jupiter": 1.8982e27, "saturn": 5.6834e26, "uranus": 8.681e25, "neptune": 1.024e26}),
        ("distance", {"mercury": 5.8e7, "venus": 1.082e8, "earth": 1.502e8, "mars": 2.279e8, "jupiter": 7.785e8, "saturn": 1.434e9, "uranus": 2.871e9, "neptune": 4.495e9}),
        ("satellites", {"mercury": 0, "venus": 0, "earth": 1, "mars": 2, "jupiter": 97, "saturn": 274, "uranus": 28, "neptune": 16}),
        ("moons", {"mercury": None, "venus": None, "earth": ["Luna"], "mars": ["Phobos", "Deimos"], "jupiter": ["Europa", "Ganymede", "Io", "Callisto"], "saturn": ["Titan", "Rhea", "Mimas", "Enceladus"], "uranus": ["Ariel", "Umbriel", "Titania", "Oberon"], "neptune": ["Triton", "Proteus"]}),
        ("radius", {"mercury": 2439.7, "venus": 6051, "earth": 6378, "mars": 3389.5, "jupiter": 69911, "saturn": 58232, "uranus": 25362, "neptune": 24622}),
        (1234, None),
        ("", None)
    ]
)
def test_get_all_planets_by_fact(input: str, expected: dict):
    """Checks that the value passed returns a dictionary of known facts for all planets

    .. test::
        :id: TTC008
        :tests: REQ006
    """
    result = solar_system_instance.get_all_planets_by_fact(input)
    assert result == expected

@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ("Earth", planet.planet("Earth")),
        (1234, None),
        ("", None)
    ]
)
def test_get_planet(input: str, expected: planet):
    """Checks that the value passed returns the correct planet object

    .. test::
        :id: TTC009
        :tests: REQ007
    """
    result = solar_system_instance.get_planet(input)
    assert result == expected


def test_get_all_planets(self) -> list[planet.planet]:
    """Checks that the function returns a list of all planet objects

    .. test::
        :id: TTC010
        :tests: REQ006
    """
    result = solar_system_instance.get_all_planets()
    assert result == [planet.planet("Mercury"),planet.planet("Venus"),planet.planet("Earth"),planet.planet("Mars"),planet.planet("Jupiter"),planet.planet("Saturn"),planet.planet("Uranus"),planet.planet("Neptune")]

# Returns a list of all planet names   
def test_get_planet_names(self) -> list[str]:
    """Checks that the value passed in can be stripped of special characters and split atomically

    .. test::
        :id: TTC011
        :tests: REQ005
    """
    result = solar_system_instance.get_planet_names()
    assert result == ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]