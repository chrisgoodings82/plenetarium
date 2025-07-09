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
    def init_planets(self):
        self.planets = []
        self.planets.append(planet.planet("Mercury"))
        self.planets.append(planet.planet("Venus"))
        self.planets.append(planet.planet("Earth"))
        self.planets.append(planet.planet("Mars"))
        self.planets.append(planet.planet("Jupiter"))
        self.planets.append(planet.planet("Saturn"))
        self.planets.append(planet.planet("Uranus"))
        self.planets.append(planet.planet("Neptune"))

    # Returns a list of all planets with the specified fact
    def get_all_planets_by_fact(self, fact):
        planet_list = {}
        for p in self.planets:
            if hasattr(p, fact):
                if fact == "moons":
                    planet_list[p.name] = p.moons_to_string()
                else:
                    # If the fact is not 'moons', we can directly access the attribute
                    # and store it in the dictionary    
                    planet_list[p.name] = getattr(p, fact)
        return planet_list

    # Retruns the planet object based on the name provided
    # If the planet is not found, it returns None
    def get_planet(self, name):
        for p in self.planets:
            if p.name.lower() == name.lower():
                return p
        return None

    # Returns a list of all planet objects
    def get_all_planets(self):
        return self.planets

    # Returns a list of all planet names   
    def get_planet_names(self):
        return [p.name for p in self.planets]
    
   