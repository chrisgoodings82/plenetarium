import random

R_PLUTO: str = "Pluto, once considered the ninth planet, is now classified as a dwarf planet. It is located in the Kuiper Belt, a region beyond Neptune, and is known for its icy surface and five moons, the largest being Charon."

def unknown() -> str:
    response = ['response | Could you please re-phrase that?',
                'response | I\'m not quite sure what you mean...',
                'response | Hmmm, that is a tough one... could you try a different question, please?'][random.randrange(3)]
    return response