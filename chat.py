#chat.py
import long_responses as long
import re
from planets import planets
from tabulate import tabulate

class chat:
    def __init__(self) -> None:
        self.planet_instance = planets()

    # Determine how close the user message is to each predefined message
    # and return the percentage of recognised words in the message.
    def message_probability(self, user_message: list[str], recognised_words: list[str], single_response: bool = False, required_words: list[str] = []) -> int:
        message_certainty: int = 0
        has_required_words: bool = True

        # Count how many words are present in each predefined message
        for word in user_message:
            if word in recognised_words:
                message_certainty += 1

        # Calculate the percent of recognised words in a user message
        percentage: float = float(message_certainty) / float(len(recognised_words))

        for word in required_words:
            if word not in user_message:
                has_required_words = False
                break
        
        # Convert to a percentage
        if has_required_words or single_response:
            return int(percentage*100)
        else:
            return 0

    # Check the user message against all predefined messages
    # and return the one with the highest probability.    
    def check_all_messages(self, message: str) -> str:
        highest_prob_list: dict = {}

        # Helper function to generate a list of the highest probability responses
        def response(bot_response: str, list_of_words: list[str], single_response: bool = False, required_words: list[str] = []) -> None:
            nonlocal highest_prob_list
            highest_prob_list[bot_response] = self.message_probability(message, list_of_words, single_response, required_words)

        # Responses ------------------------------------------------------------------------------------------------------
        # Response: Action | Detail | Fact | Planet | Message
        # Salutations
        response("response | Hello!", ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
        response("response | I\'m doing fine, and you?", ['how', 'are', 'you', 'doing'], required_words= ['how'])
        response("response | Goodbye!", ['Goodbye', 'bye', 'quit'], single_response=True)

        # Direct Responses
        response(f"response | {long.R_PLUTO}", ['is', 'pluto', 'a', 'planet'], required_words= ['pluto', 'planet'])
        
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
        response(f"display | fact | mass | mercury", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'mercury'], required_words= ['mercury'])
        response(f"display | fact | distance | mercury", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'mercury'], required_words= ['mercury'])
        response(f"display | fact | satellites | mercury", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'mercury'], required_words= ['mercury'])
        response(f"display | fact | moons | mercury", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'mercury'], required_words= ['mercury', 'moons'])
        response(f"display | fact | radius | mercury", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'mercury'], required_words= ['mercury'])

        # Display data about venus
        response(f"display | all | all | venus", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'venus'], required_words= ['venus'])
        response(f"display | fact | mass | venus", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'venus'], required_words= ['venus'])
        response(f"display | fact | distance | venus", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'venus'], required_words= ['venus'])
        response(f"display | fact | satellites | venus", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'venus'], required_words= ['venus'])
        response(f"display | fact | moons | venus", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'venus'], required_words= ['venus', 'moons'])
        response(f"display | fact | radius | venus", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'venus'], required_words= ['venus'])

        # Display data about earth
        response(f"display | all | all | earth", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'earth'], required_words= ['earth'])
        response(f"display | fact | mass | earth", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'earth'], required_words= ['earth'])
        response(f"display | fact | distance | earth", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'earth'], required_words= ['earth'])
        response(f"display | fact | satellites | earth", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'earth'], required_words= ['earth'])
        response(f"display | fact | moons | earth", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'earth'], required_words= ['earth', 'moons'])
        response(f"display | fact | radius | earth", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'earth'], required_words= ['earth'])

        # Display data about mars
        response(f"display | all | all | mars", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'mars'], required_words= ['mars'])
        response(f"display | fact | mass | mars", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'mars'], required_words= ['mars'])
        response(f"display | fact | distance | mars", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'mars'], required_words= ['mars'])
        response(f"display | fact | satellites | mars", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'mars'], required_words= ['mars'])
        response(f"display | fact | moons | mars", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'mars'], required_words= ['mars', 'moons'])
        response(f"display | fact | radius | mars", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'mars'], required_words= ['mars'])

        # Display data about jupiter
        response(f"display | all | all | jupiter", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'jupiter'], required_words= ['jupiter'])
        response(f"display | fact | mass | jupiter", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'jupiter'], required_words= ['jupiter'])
        response(f"display | fact | distance | jupiter", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'jupiter'], required_words= ['jupiter'])
        response(f"display | fact | satellites | jupiter", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'jupiter'], required_words= ['jupiter'])
        response(f"display | fact | moons | jupiter", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'jupiter'], required_words= ['jupiter', 'moons'])
        response(f"display | fact | radius | jupiter", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'jupiter'], required_words= ['jupiter'])

        # Display data about saturn
        response(f"display | all | all | saturn", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'saturn'], required_words= ['saturn'])
        response(f"display | fact | mass | saturn", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'saturn'], required_words= ['saturn'])
        response(f"display | fact | distance | saturn", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'saturn'], required_words= ['saturn'])
        response(f"display | fact | satellites | saturn", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'saturn'], required_words= ['saturn'])
        response(f"display | fact | moons | saturn", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'saturn'], required_words= ['saturn', 'moons'])
        response(f"display | fact | radius | saturn", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'saturn'], required_words= ['saturn'])

        # Display data about uranus
        response(f"display | all | all | uranus", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'uranus'], required_words= ['uranus'])
        response(f"display | fact | mass | uranus", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'uranus'], required_words= ['uranus'])
        response(f"display | fact | distance | uranus", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'uranus'], required_words= ['uranus'])
        response(f"display | fact | satellites | uranus", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'uranus'], required_words= ['uranus'])
        response(f"display | fact | moons | uranus", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'uranus'], required_words= ['uranus', 'moons'])
        response(f"display | fact | radius | uranus", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'uranus'], required_words= ['uranus'])

        # Display data about neptune
        response(f"display | all | all | neptune", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'neptune'], required_words= ['neptune'])
        response(f"display | fact | mass | neptune", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'neptune'], required_words= ['neptune'])
        response(f"display | fact | distance | neptune", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'neptune'], required_words= ['neptune'])
        response(f"display | fact | satellites | neptune", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'neptune'], required_words= ['neptune'])
        response(f"display | fact | moons | neptune", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'neptune'], required_words= ['neptune', 'moons'])
        response(f"display | fact | radius | neptune", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'neptune'], required_words= ['neptune'])

        # Provide comparrison data
        response(f"compare | all | all | all", ['compare', 'all', 'everything', 'about', 'relating', 'to', 'all', 'planets'], required_words= ['compare', 'all', 'planets'])
        response(f"compare | fact | mass | all", ['compare', 'mass', 'weight', 'how', 'massive', 'of', 'all', 'planets'], required_words= ['compare', 'mass', 'planets'])
        response(f"compare | fact | distance | all", ['compare', 'distance', 'how', 'far','from', 'the','sun', 'of', 'all', 'planets'], required_words= ['compare', 'distance', 'planets'])
        response(f"compare | fact | satellites | all", ['compare', 'satellitees', 'of', 'all', 'planets'], required_words= ['compare', 'satellites', 'planets'])
        response(f"compare | fact | moons | all", ['compare', 'the', 'moons', 'of', 'all', 'planets'], required_words= ['compare', 'planets', 'moons'])
        response(f"compare | fact | radius | all", ['compare', 'radius', 'of', 'all', 'planets'], required_words= ['compare', 'radius', 'planets'])

        best_match: str = max(highest_prob_list, key=highest_prob_list.get)
        #print(highest_prob_list)

        return long.unknown() if highest_prob_list[best_match] < 1 else best_match                  # End: check_all_messages

    def split_response(self, response: str) -> list[str]:
        return response.split("|")

    # Display the data for a planet or all planets
    # If the fact is "all", then all data is displayed, else only the specified fact is displayed.
    # If the planet is "all", then all planets are displayed, else only the specified planet    
    def display_fact(self, response) -> str:
        split_response_string: list[str] = self.split_response(response)
        fact: str = split_response_string[2].strip()
        planet: str = split_response_string[3].strip()
        output: str = ""
        if fact == "all":           
            if planet == "all":     # Display all data for all planets
                for item in self.planet_instance.get_all_planets():
                    output += item.display_all_data()
            else:                   # Display all data for a specific planet
                planets_output: list[str] = [p for p in self.planet_instance.get_all_planets() if p.name.lower() == planet.lower()]
                output += planets_output[0].display_all_data()
        else:
            if planet == "all":     # Display a specific fact for all planets
                for item in self.planet_instance.get_all_planets():
                    output += item.display_fact(fact)
            else:                   # Display a specific fact for a specific planet 
                planets_output: list[str] = self.planet_instance.get_planet(planet)
                output += planets_output.display_fact(fact)
        return output

    # Compare the specified fact for all planets or a specific planet
    # If the fact is "all", then all data is displayed, else only the specified fact   
    # If the planet is "all", then all planets are displayed, else only the specified planet
    def compare_fact(self, response: str) -> str:
        split_response_string: list[str] = self.split_response(response)
        fact: str = split_response_string[2].strip()
        #planet_selection: str = split_response_string[3].strip()
        planet_list: list = []
        if fact == "all":
            for planet in self.planet_instance.get_all_planets():
                    planet_list.append(planet.export_data())
            return f"\n{tabulate(planet_list, ['Name', 'Mass (kg)', 'Distance (km)', 'Satelites', 'Moons', 'Radius (km)'], tablefmt='grid')}"
        else:
            for planet in self.planet_instance.get_all_planets():
                    if hasattr(planet, fact):
                        planet_list.append(planet.export_fact(fact))
            if fact in ['distance', 'radius']:
                unit = ' (km)'
            elif fact == 'mass':
                unit = ' (kg)'
            else:
                unit = ''
            return f"\n{tabulate(planet_list, ['Name', f"{fact}{unit}" ], tablefmt='grid')}"

    # Parse the response based on the type of response   
    def response_parser(self, response: str) -> str:
        if "display" in response:
            return self.display_fact(response)
        if "response" in response:
            return response[11:]
        if "compare" in response:
            return self.compare_fact(response)

    # Get the response from the user input, split it into words, and check against all messages
    # Return the parsed response as a string
    def get_response(self, user_input: str) -> str:
        split_message: list[str] = re.split(r'\s+|[?.,\';:-]\s*', user_input.lower())
        response:str = self.check_all_messages(split_message)
        parsed_response: str = self.response_parser(response)
        return parsed_response