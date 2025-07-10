# planet.py
import json

class planet:
    """Planet Class

        Parameters:
            name: The name of the planet to be instantiated.

        .. impl::
            :id: PLANET
            :implements: REQ_09
    """
    def __init__(self, name: str):
        with open('planets.json', 'r') as file:
            data = json.load(file)
        
        for planet in data['planets']:
            if planet['name'] == name:
                self.name: str = planet["name"]
                self.mass: float = float(planet["mass"])
                self.distance: float = float(planet["distance"])
                self.satellites: int = int(planet["satellites"])
                self.moons: list[str] = planet["moons"]
                self.radius: float = float(planet["radius"])
                break
    
    def moons_to_string(self) -> str:
        """Converts the list of moons to a formatted string

        Returns:
            A formated string containing the list of moons

        .. impl::
            :id: MOONS_TO_STRING
            :implements: REQ_10
        """
        if len(self.moons) == 0:
            return ""
        elif len(self.moons) == 1:
            return self.moons[0]
        else:
            output: str = ""
            for index, item in enumerate(self.moons):
                if index == len(self.moons) - 1:
                    output += item
                else:
                    output += item + ", "
            return output

    def display_all_data(self) -> str:
        """Displays all data abot a planet as a formatted string.

        Returns:
            A formated string containing the data about a planet.

        .. impl::
            :id: DISPLAY_ALL_DATA
            :implements: REQ_08
        """
        output: str = f"The planet {self.name} is positioned {self.distance} km from the Sun. It has a mass of {self.mass} kg, a radius of {self.radius} km. "
        output += f"{self.name} has {self.satellites} moon{'s' if int(self.satellites) != 1 else ''}."
        
        if int(self.satellites) != 0:
            if int(self.satellites) == 1:
                output += "This is: "
            elif int(self.satellites) < 3:
                output += "These are: "
            elif int(self.satellites) >= 3:
                output += "The notable ones are: "
            output += self.moons_to_string()
        return output + "\n"

    def display_fact(self, fact: str) -> str:
        """Displays a formated string about a specific fact relating to the planet.

        Args:
            fact: The fact to be displayed (mass, distance, satellites, moons, radius)

        Returns:
            A formated string containing the fact about the planet.

        .. impl::
            :id: DISPLAY_PLANET_FACT
            :implements: REQ_01
        """
        initial: str = f"The planet {self.name} "
        match fact:
            case "mass":
                body: str = f"has a mass of {self.mass} kg. "
            case "distance":
                body: str = f"is {self.distance} km from the Sun. "
            case "satellites":
                body: str = f"has {self.satellites} moons. "
            case "moons":
                body: str = f"has the following moons: {self.moons_to_string()}. "
            case "radius":
                body: str = f"has a radius of {self.radius} km. "
            
        return f"{initial}{body}"
    
    def export_data(self) -> list:
        """Provides a list of all facts as raw data.

        Returns:
            A list of all facts as raw data.

        .. impl::
            :id: EXPORT_DATA
            :implements: REQ_04
        """
        return [self.name, self. mass, self.distance, self.satellites, self.moons_to_string(), self.radius]
    
    def export_fact(self, fact: str) -> list[str]:
        """Provides a list containing the name of the planet and the desired fact.

        Args:
            fact: The fact to be displayed (mass, distance, satellites, moons, radius)

        Returns:
            A list containing the planet name and the value associated with the fact.

        .. impl::
            :id: EXPORT_PLANET_FACT
            :implements: REQ_08
        """
        if hasattr(self, fact):
            return [self.name, self.__getattribute__(fact)]