import planet

class planets:

    _instance = None
    # Constructor to initialize the planets list with the eight major planets
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(planets, cls).__new__(cls)
            cls._instance.init_planets()

        return cls._instance
    
    # Initializes the planets list with the eight major planets
    def init_planets(self) -> None:
        self.planets = []
        self.planets.append(planet.planet("Mercury"))
        self.planets.append(planet.planet("Venus"))
        self.planets.append(planet.planet("Earth"))
        self.planets.append(planet.planet("Mars"))
        self.planets.append(planet.planet("Jupiter"))
        self.planets.append(planet.planet("Saturn"))
        self.planets.append(planet.planet("Uranus"))
        self.planets.append(planet.planet("Neptune"))

    # Returns a dictionary of all planets with the specified fact
    def get_all_planets_by_fact(self, fact: str) -> dict:
        planet_list: dict = {}
        for local_planet in self.planets:
            if hasattr(local_planet, fact):
                if fact == "moons":
                    planet_list[local_planet.name] = local_planet.moons_to_string()
                else:
                    # If the fact is not 'moons', we can directly access the attribute
                    # and store it in the dictionary    
                    planet_list[local_planet.name] = getattr(local_planet, fact)
        return planet_list

    # Retruns the planet object based on the name provided
    # If the planet is not found, it returns None
    def get_planet(self, name: str) -> planet:
        for local_planet in self.planets:
            if local_planet.name.lower() == name.lower():
                return local_planet
        return None

    # Returns a list of all planet objects
    def get_all_planets(self) -> list[planet.planet]:
        return self.planets

    # Returns a list of all planet names   
    def get_planet_names(self) -> list[str]:
        return [local_planet.name for local_planet in self.planets]
    
   