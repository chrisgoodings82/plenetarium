from contextlib import nullcontext as does_not_raise
import pytest
import scripts.response as response


Expectation = pytest.RaisesExc | does_not_raise



@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ([["tell", "me", "about", "mars"], ["tell", "me", "about", "mars"], False, ["mars"] ], 100),
        ([["tell", "me", "about", "mars"], ["tell", "me", "about", "mars"], False, ["earth"] ], 0),
        ([["tell", "me", "about", "mars"], ["tell", "me", "about", "mars"], True, ["mars"] ], 100),
        ([["tell", "me", "about", "mars"], ["tell", "me", "about", "mars"], True, ["earth"] ], 100),
        ([["tell", "me", "about", "mars"], ["wish", "upon", "a", "star"], False, ["mars"] ], 0),
        ([["tell", "me", "about", "mars"], ["wish", "upon", "a", "star"], True, [] ], 0),
        ([["tell", "me", "about", "mars"], ["tell", "me", "a", "star"], False, ["mars"] ], 50)
    ]
)
def test_message_probability(input: list, expected: int):
    """Checks that the message probability function returns a valid probability score

    .. test::
        :id: TTC005
        :tests: REQ001
    """
    result = response.message_probability(input[0], input[1], input[2], input[3])
    assert result == expected

@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        (["tell", "me", "about", "mars"], "display | fact | mass | all"),
        (["hello"], "response | Hello!"),
        (["bye"], "response | Goodbye!"),
        (["pluto"], "response |p Pluto, once considered the ninth planet, is now classified as a dwarf planet. It is located in the Kuiper Belt, a region beyond Neptune, and is known for its icy surface and five moons, the largest being Charon."),
        (["moon", "phases"], "response |j Full moon, Half moon, New moon..."),
        (["largest", "moon"], "response |s That's no moon!!!"),
    ]
)
def test_check_all_messages(input: list[str], expected: str):
    """Checks that the check_all_messages function returns the expected response

    .. test::
        :id: TTC006
        :tests: REQ002
    """
    result = response.check_all_messages(input)
    assert result == expected
     
@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ("display | fact | mass | all", ["display", "fact", "mass", "all"]),
        ("hello", ["hello"]),
        ("", []),
    ]
)      
def test_split_response(input: str, expected: list[str]):
    """Checks that the split_response function returns a list of words from the response string

    .. test::
        :id: TTC007
        :tests: REQ003
    """
    result = response.split_response(input)
    assert result == expected   
