import scripts.planet as planet

class solar_system:
    """A singleton planets class that has only one instance across the application. 
    A singleton pattern was chosen as there will only ever need to be a single instance
    and it will also allow me to access the planets list data.

    .. impl::
        :id: PLANETS
        :implements: REQ001
        :tests: TTC001
    """

    _instance = None

    def __new__(cls):
        """Responsible for creating a new instance of the class.
            [1] https://www.geeksforgeeks.org/python/__new__-in-python/

        :param class cls: The class itself

        :return: An instance of the class
        :rtype: class

        .. impl::
            :id: SOLAR_SYSTEM_NEW_INSTANCE
            :implements: REQ001
            :tests: TTC001
        """
        if cls._instance is None:
            cls._instance = super(solar_system, cls).__new__(cls)
            cls._instance.init_solar_system()

        return cls._instance
    
    def init_solar_system(self) -> None:
        """Instantiates all of the planets and stores them to a list that can be globally accessed through the instance

        .. impl::
            :id: SOLAR_SYSTEM_INIT_PLANETS
            :implements: REQ001
            :tests: TTC001
        """
        self.planets = []
        self.planets.append(planet.planet("Mercury"))
        self.planets.append(planet.planet("Venus"))
        self.planets.append(planet.planet("Earth"))
        self.planets.append(planet.planet("Mars"))
        self.planets.append(planet.planet("Jupiter"))
        self.planets.append(planet.planet("Saturn"))
        self.planets.append(planet.planet("Uranus"))
        self.planets.append(planet.planet("Neptune"))

    def get_all_planets_by_fact(self, fact: str) -> dict:
        """Gets all planets and the associated fact

        :param str fact: The fact to be displayed (mass, distance, satellites, moons, radius)

        :return: A dictionary of each planet and the associated fact value.
        :rtype: dict

        .. impl::
            :id: SOLAR_SYSTEM_GET_ALL_PLANETS_BY_FACT
            :implements: REQ001
            :tests: TTC001
        """
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

    def get_planet(self, name: str) -> planet:
        """Gets the planet object based on its name.

        :param str name: The name of the planet.

        :return: The planet object
        :rtype: planet

        .. impl::
            :id: SOLAR_SYSTEM_GET_PLANET
            :implements: REQ001
            :tests: TTC001
        """
        for local_planet in self.planets:
            if local_planet.name.lower() == name.lower():
                return local_planet
        return None

    def get_all_planets(self) -> list[planet.planet]:
        """Gets a list of all planets as objects.

        :returns: A list of planet objects.
        :rtype: list[planet]
        
        .. impl::
            :id: SOLAR_SYSTEM_GET_ALL_PLANETS
            :implements: REQ001
            :tests: TTC001
        """
        return self.planets

    # Returns a list of all planet names   
    def get_planet_names(self) -> list[str]:
        """Gets a list of all of the planet names.

        :returns: A list of the planets names.
        :rtype: list[str]

        .. impl::
            :id: SOLAR_SYSTEM_GET_PLANET_NAMES
            :implements: REQ001
            :tests: TTC001
        """
        return [local_planet.name for local_planet in self.planets]
    
   