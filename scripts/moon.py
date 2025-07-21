# planet.py
import os
import json

class moon:
    def __init__(self, name: str) -> None:
        """Moon Class constructor

        :param str name: The name of the moon to be instantiated.

        .. impl::
            :id: MOON_INIT
            :implements: REQ001
            :tests: TTC001
        """
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        ROOT_DIR = ROOT_DIR.replace('scripts', 'data')
        with open(ROOT_DIR + '/planets.json', 'r') as file:
            data = json.load(file)
        
        found = False
        for planet in data['planets']:
            for vMoon in planet['moons']:
                if vMoon == name:
                    self.name: str = planet['moons'][name]["name"]
                    self.mass: float = float(planet['moons'][name]["mass"])
                    self.distance: float = float(planet['moons'][name]["distance"])
                    self.radius: float = float(planet['moons'][name]["radius"])
                    self.image: str = planet['moons'][name]["image"]
                    found = True
                    break
            if found:
                break

    def get_name(self):
        return self.name