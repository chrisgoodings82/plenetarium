# planet.py
import json
import os
import scripts.moon as moon

class moon:
    """Planet Class

        Parameters:
            name: The name of the planet to be instantiated.

        .. impl::
            :id: PLANET
            :implements: REQ_09
    """
    def __init__(self, name: str):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        ROOT_DIR = ROOT_DIR.replace('scripts', 'data')
        with open(ROOT_DIR + '/planets.json', 'r') as file:
            data = json.load(file)
        
        for moon in data['planets']['moons']:
            if moon['name'] == name:
                self.name: str = moon["name"]
                self.mass: float = float(moon["mass"])
                self.distance: float = float(moon["distance"])
                self.radius: float = float(moon["radius"])
                self.image: str = moon["image"]
                break

    def export_data(self) -> list:
        """Provides a list of all facts as raw data.

        Returns:
            A list of all facts as raw data.

        .. impl::
            :id: EXPORT_DATA
            :implements: REQ_04
        """
        return [self.name, self. mass, self.distance, self.radius, self.image]