import random
from tabulate import tabulate
import utilities.long_responses as long
import utilities.utils as utils
import scripts.planet as planet
import scripts.solar_system as planets

planet_instance = planets.solar_system()

def message_probability(user_message: list[str], recognised_words: list[str], single_response: bool = False, required_words: list[str] = []) -> int:
        """Calculate the probability that user entered messages match the desired terms.

        Args:
            user_message: The user's sanitized message split into a list.
            recognised_words: A list of terms that the user message is to be matched against.
            single_response: Will a single term be matched from the recognised words.
            required_words: A list of the words that must be present in the user message.

        Returns:
            The percentage probability that a user message matches the required words.

        .. impl::
            :id: MESSAGE_PROBABILITY
            :implements: REQ_03, REQ_04
        
        """
        message_certainty: int = 0
        has_required_words: bool = True

        for word in user_message:
            if word in recognised_words:
                message_certainty += 1

        percentage: float = float(message_certainty) / float(len(recognised_words))

        for word in required_words:
            if word not in user_message:
                has_required_words = False
                break
        
        if has_required_words or single_response:
            return int(percentage*100)
        else:
            return 0
    
def check_all_messages(message: list[str]) -> str:
    """Checks all of the individual user terms to determine which response is the closest match.
        ACTION: DISPLAY, RESPONSE, COMPARE
        DETAIL: ALL, FACT, VALUE (Value is the raw output to be displayed)
        FACT: DISTANCE, MASS, SATELLITES, MOONS, RADIUS, ALL
        PLANET: MERCURY, VENUS, EARTH, MARS, JUPITER, SATURN, URANUS, NEPTUNE, ALL

        Args:
            message: The sanitised and split list of atomic terms provided by the user.

        Returns:
            A structured response as a string, in the format: ACTION | DETAIL | FACT | PLANET or
            ACTION | DETAIL

        .. impl::
            :id: CHECK_ALL_MESSAGES
            :implements: REQ_09
    """    
    highest_prob_list: dict = {}

    # Helper function to generate a list of the highest probability responses
    def response(structured_response: str, list_of_words: list[str], single_response: bool = False, required_words: list[str] = []) -> None:
        """Determines the highest probability response based on the closest match in terms.

        Args:
            structured_response: The structured response that will be returned if a match is made.
            list_of_words: These are response flags that will be used to compare the user's terms to.
            single_response: Identifies if only a single word is to be matched from the list of words.
            requuired_words: Words that must be included in the user's input for a match to be considered.

        .. impl::
            :id: RESPONSE
            :implements: REQ_10
    """   
        nonlocal highest_prob_list
        highest_prob_list[structured_response] = message_probability(message, list_of_words, single_response, required_words)

    ######################################################################################################################################
    #################################################### RESPONSES #######################################################################
    ######################################################################################################################################
    
    response("response | Hello!", ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response("response | I\'m doing fine, and you?", ['how', 'are', 'you', 'doing'], required_words= ['how'])
    response("response | Goodbye!", ['goodbye', 'bye', 'good bye', ':q', 'quit'], single_response=True)

    # Direct Responses
    response(f"response |p {long.R_PLUTO}", ['is', 'pluto', 'a', 'planet'], required_words= ['pluto', 'planet'])
    response(f"response |s That's no moon!!!", ['what', 'is', 'the', 'largest', 'moon'], required_words= ['what', 'is', 'the', 'largest', 'moon'])
    response(f"response |j Full moon, Half moon, New moon...", ['what', 'are', 'the', 'phases','of','the','moon'], required_words= ['what', 'are', 'the', 'phases','of','the','moon'])
    
    # Display all data about all planets
    response(f"display | all | all | all", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'planets'], required_words= ['planets'])

    # Display specific facts about all planets
    response(f"display | fact | mass | all", ['tell', 'me', 'show', 'display', 'mass', 'present', 'all', 'everything', 'about', 'relating', 'to', 'planets'], required_words= ['planets', 'mass'])
    response(f"display | fact | distance | all", ['tell', 'me', 'show', 'display', 'distance', 'present', 'all', 'everything', 'about', 'relating', 'to', 'planets'], required_words= ['planets', 'distance'])
    response(f"display | fact | satellites | all", ['tell', 'me', 'show', 'display', 'satellites', 'present', 'all', 'everything', 'about', 'relating', 'to', 'planets'], required_words= ['planets', 'satellites'])
    response(f"display | fact | moons | all", ['tell', 'me', 'show', 'display', 'moons', 'present', 'all', 'everything', 'about', 'relating', 'to', 'planets'], required_words= ['planets', 'moons'])
    response(f"display | fact | radius | all", ['tell', 'me', 'show', 'display', 'radius', 'present', 'all', 'everything', 'about', 'relating', 'to', 'planets'], required_words= ['planets', 'radius'])

    # Display data about mercury
    response(f"display | all | all | mercury", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'mercury'], required_words= ['mercury'])
    response(f"display | fact | mass | mercury", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'mercury'], required_words= ['mercury', 'mass'])
    response(f"display | fact | distance | mercury", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'mercury'], required_words= ['mercury', 'distance'])
    response(f"display | fact | satellites | mercury", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'mercury'], required_words= ['mercury', 'satellites'])
    response(f"display | fact | moons | mercury", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'mercury'], required_words= ['mercury', 'moons'])
    response(f"display | fact | radius | mercury", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'mercury'], required_words= ['mercury', 'radius'])

    # Display data about venus
    response(f"display | all | all | venus", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'venus'], required_words= ['venus'])
    response(f"display | fact | mass | venus", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'venus'], required_words= ['venus', 'mass'])
    response(f"display | fact | distance | venus", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'venus'], required_words= ['venus', 'distance'])
    response(f"display | fact | satellites | venus", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'venus'], required_words= ['venus', 'satellites'])
    response(f"display | fact | moons | venus", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'venus'], required_words= ['venus', 'moons'])
    response(f"display | fact | radius | venus", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'venus'], required_words= ['venus', 'radius'])

    # Display data about earth
    response(f"display | all | all | earth", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'earth'], required_words= ['earth'])
    response(f"display | fact | mass | earth", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'earth'], required_words= ['earth', 'mass'])
    response(f"display | fact | distance | earth", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'earth'], required_words= ['earth', 'distance'])
    response(f"display | fact | satellites | earth", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'earth'], required_words= ['earth', 'satellites'])
    response(f"display | fact | moons | earth", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'earth'], required_words= ['earth', 'moons'])
    response(f"display | fact | radius | earth", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'earth'], required_words= ['earth', 'radius'])

    # Display data about mars
    response(f"display | all | all | mars", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'mars'], required_words= ['mars'])
    response(f"display | fact | mass | mars", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'mars'], required_words= ['mars', 'mass'])
    response(f"display | fact | distance | mars", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'mars'], required_words= ['mars', 'distance'])
    response(f"display | fact | satellites | mars", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'mars'], required_words= ['mars', 'satellites'])
    response(f"display | fact | moons | mars", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'mars'], required_words= ['mars', 'moons'])
    response(f"display | fact | radius | mars", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'mars'], required_words= ['mars', 'radius'])

    # Display data about jupiter
    response(f"display | all | all | jupiter", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'jupiter'], required_words= ['jupiter'])
    response(f"display | fact | mass | jupiter", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'jupiter'], required_words= ['jupiter', 'mass'])
    response(f"display | fact | distance | jupiter", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'jupiter'], required_words= ['jupiter', 'distance'])
    response(f"display | fact | satellites | jupiter", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'jupiter'], required_words= ['jupiter', 'satellites'])
    response(f"display | fact | moons | jupiter", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'jupiter'], required_words= ['jupiter', 'moons'])
    response(f"display | fact | radius | jupiter", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'jupiter'], required_words= ['jupiter', 'radius'])

    # Display data about saturn
    response(f"display | all | all | saturn", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'saturn'], required_words= ['saturn'])
    response(f"display | fact | mass | saturn", ['what', 'is', 'of', 'tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'saturn'], required_words= ['saturn', 'mass'])
    response(f"display | fact | distance | saturn", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'saturn'], required_words= ['saturn', 'distance'])
    response(f"display | fact | satellites | saturn", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'saturn'], required_words= ['saturn', 'satellites'])
    response(f"display | fact | moons | saturn", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'saturn'], required_words= ['saturn', 'moons'])
    response(f"display | fact | radius | saturn", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'saturn'], required_words= ['saturn', 'radius'])

    # Display data about uranus
    response(f"display | all | all | uranus", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'uranus'], required_words= ['uranus'])
    response(f"display | fact | mass | uranus", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'uranus'], required_words= ['uranus', 'mass'])
    response(f"display | fact | distance | uranus", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'uranus'], required_words= ['uranus', 'distance'])
    response(f"display | fact | satellites | uranus", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'uranus'], required_words= ['uranus', 'satellites'])
    response(f"display | fact | moons | uranus", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'uranus'], required_words= ['uranus', 'moons'])
    response(f"display | fact | radius | uranus", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'uranus'], required_words= ['uranus', 'radius'])

    # Display data about neptune
    response(f"display | all | all | neptune", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'neptune'], required_words= ['neptune'])
    response(f"display | fact | mass | neptune", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'neptune'], required_words= ['neptune', 'mass'])
    response(f"display | fact | distance | neptune", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'neptune'], required_words= ['neptune', 'distance'])
    response(f"display | fact | satellites | neptune", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'neptune'], required_words= ['neptune', 'satellites'])
    response(f"display | fact | moons | neptune", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'neptune'], required_words= ['neptune', 'moons'])
    response(f"display | fact | radius | neptune", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'neptune'], required_words= ['neptune', 'radius'])

    # Provide comparrison data
    response(f"compare | all | all | all", ['compare', 'all', 'everything', 'about', 'relating', 'to', 'all', 'planets'], required_words= ['compare', 'all', 'planets'])
    response(f"compare | fact | mass | all", ['compare', 'mass', 'weight', 'how', 'massive', 'of', 'all', 'planets'], required_words= ['compare', 'mass', 'planets'])
    response(f"compare | fact | distance | all", ['compare', 'distance', 'how', 'far','from', 'the','sun', 'of', 'all', 'planets'], required_words= ['compare', 'distance', 'planets'])
    response(f"compare | fact | satellites | all", ['compare', 'satellitees', 'of', 'all', 'planets'], required_words= ['compare', 'satellites', 'planets', 'satellites'])
    response(f"compare | fact | moons | all", ['compare', 'the', 'moons', 'of', 'all', 'planets'], required_words= ['compare', 'planets', 'moons'])
    response(f"compare | fact | radius | all", ['compare', 'radius', 'of', 'all', 'planets'], required_words= ['compare', 'radius', 'planets'])

    best_match: str = max(highest_prob_list, key=highest_prob_list.get)

    return long.R_UNKNOWN[random.randrange(3)] if highest_prob_list[best_match] < 1 else best_match                  # End: check_all_messages


def split_response(response: str) -> list[str]:
    """Splits the user response

    Args:
        response: The response that has been returned as the closest match.

    Returns:
        A list of the response terms.

    .. impl::
        :id: SPLIT_RESPONSE
        :implements: REQ_05

    """
    return response.split("|")

def set_image(planet: str):
    utils.PLANET_IMAGE =  f'data\\images\\{planet}.png'
    pass

def display_fact(response: str) -> str:
    """Displays a formatted string about a specific fact

    Args:
        response: The response that has been returned as the closest match.

    Returns:
        A formated string containing information about a specific fact

    .. impl::
        :id: DISPLAY_FACT
        :implements: REQ_06

    """
    split_response_string: list[str] = split_response(response)
    fact: str = split_response_string[2].strip()
    planet: str = split_response_string[3].strip()
    output: str = ""
    if fact == "all":           
        if planet == "all":     # Display all data for all planets
            for item in planet_instance.get_all_planets():
                output += item.display_all_data()
            set_image("planets\solarsystem")
        else:                   # Display all data for a specific planet
            planets_output: list[str] = [p for p in planet_instance.get_all_planets() if p.name.lower() == planet.lower()]
            output += planets_output[0].display_all_data()
            set_image(f'planets\\{planet.lower()}')
    else:
        if planet == "all":     # Display a specific fact for all planets
            for item in planet_instance.get_all_planets():
                output += item.display_fact(fact)
            set_image("planets\solarsystem")
        else:                   # Display a specific fact for a specific planet 
            planets_output: list[str] = planet_instance.get_planet(planet)
            output += planets_output.display_fact(fact)
            set_image(f'planets\\{planet.lower()}')
    return output

def compare_fact(response: str) -> str:
    """Displays a formatted table comparing all facts, or a specific fact.

    Args:
        response: The response that has been returned as the closest match.

    Returns:
        A formated table containing information about a specific fact

    .. impl::
        :id: COMPARE_FACT
        :implements: REQ_11, REQ_12

    """
    set_image("planets\solarsystem")
    split_response_string: list[str] = split_response(response)
    fact: str = split_response_string[2].strip()
    planet_list: list = []
    if fact == "all":
        for planet in planet_instance.get_all_planets():
                planet_list.append(planet.export_data())
        return f"\n{tabulate(planet_list, ['Name', 'Mass\n(kg)', 'Distance\n(km)', 'Satellites', 'Moons', 'Radius\n(km)'], tablefmt='grid', maxcolwidths=[20,20,20,20,20,20])}"
    else:
        for planet in planet_instance.get_all_planets():
                if hasattr(planet, fact):
                    planet_list.append(planet.export_fact(fact))
        if fact in ['distance', 'radius']:
            unit = ' (km)'
        elif fact == 'mass':
            unit = ' (kg)'
        else:
            unit = ''
        return f"\n{tabulate(planet_list, ['Name', f"{fact}{unit}" ], tablefmt='grid', maxcolwidths=[None, 20])}"
    
def display_individual_response(response: str) -> str:
    if response[10] == 'p':
        set_image("planets\pluto")
    elif response[10] == 's':
        set_image("moons\deathstar")
    elif response[10] == 'j':
        set_image("moons\halfmoon")
    return response[12:]
def response_parser(response: str) -> str:
    """Parses the matched response to determine if the resonse is a direct one, if it
    requires facts to be displayed, or whether the data should be compared and tabulated.

    Args:
        response: The response that has been returned as the closest match.

    Returns:
        A formated string containing the parsed response

    .. impl::
        :id: RESPONSE_PARSER
        :implements: REQ_07
    """
    if "display" in response:
        return display_fact(response)
    if "response" in response:
        return display_individual_response(response)
    if "compare" in response:
        return compare_fact(response)
    
def get_response(user_input: str) -> str:
        split_message = utils.sanitize_query(user_input)
        response = check_all_messages(split_message)           # Gets the response key terms
        return response_parser(response)