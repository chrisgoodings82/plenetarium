# planet.py
import json

class planet:

    def __init__(self, name):
        with open('planets.json', 'r') as file:
            data = json.load(file)
        
        for planet in data['planets']:
            if planet['name'] == name:
                self.name: str = planet["name"]
                self.mass: float = float(planet["mass"])
                self.distance = planet["distance"]
                self.satellites = planet["satellites"]
                self.moons = planet["moons"]
                self.radius = planet["radius"]
                break
    
    def moons_to_string(self):
        if len(self.moons) == 0:
            return ""
        elif len(self.moons) == 1:
            return self.moons[0]
        else:
            output = ""
            for index, item in enumerate(self.moons):
                if index == len(self.moons) - 1:
                    output += item
                else:
                    output += item + ", "
            return output

    def display_all_data(self):
        output = f"The planet {self.name} is positioned {self.distance} km from the Sun. It has a mass of {self.mass} kg, a radius of {self.radius} km. "
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

    def display_fact(self, fact):
        initial = f"The planet {self.name} "
        match fact:
            case "mass":
                body = f"has a mass of {self.mass} kg. "
            case "distance":
                body = f"is {self.distance} km from the Sun. "
            case "satellites":
                body = f"has {self.satellites} moons. "
            case "moons":
                body = f"has the following moons: {self.moons_to_string()}. "
            case "radius":
                body = f"has a radius of {self.radius} km. "
            
        return f"{initial}{body}"
    
    def export_data(self):
        return [self.name, self. mass, self.distance, self.satellites, self.moons_to_string(), self.radius]
    
    def export_fact(self, fact):
        if hasattr(self, fact):
            return [self.name, self.__getattribute__(fact)]