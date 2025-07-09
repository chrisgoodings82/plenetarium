#chat.py
import scripts.long_responses as long
import re
from scripts.planets import planets
from tabulate import tabulate

class chat:
    """Planetarium chatbot

    .. impl::
        :id: PLANITARIUM_CHATBOT
        :implements: REQ_01, REQ_02
    """
    def __init__(self) -> None:
        self.planet_instance = planets()

    

    def split_response(self, response: str) -> list[str]:
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
  
    def display_fact(self, response: str) -> str:
        """Displays a formatted string about a specific fact

        Args:
            response: The response that has been returned as the closest match.

        Returns:
            A formated string containing information about a specific fact

        .. impl::
            :id: DISPLAY_FACT
            :implements: REQ_06

        """
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

    def compare_fact(self, response: str) -> str:
        """Displays a formatted table comparing all facts, or a specific fact.

        Args:
            response: The response that has been returned as the closest match.

        Returns:
            A formated table containing information about a specific fact

        .. impl::
            :id: COMPARE_FACT
            :implements: REQ_11, REQ_12

        """
        split_response_string: list[str] = self.split_response(response)
        fact: str = split_response_string[2].strip()
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
 
    def response_parser(self, response: str) -> str:
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
            return self.display_fact(response)
        if "response" in response:
            return response[11:]
        if "compare" in response:
            return self.compare_fact(response)

    def get_response(self, user_input: str) -> str:
        """
        Gets the response from the user, sanitises it of special characters, and then splits the sentence
        into atomic parts. These are then processed to return the highest probability matched response string.
        This response is then directed to the most appropriate parser, which returns a formated string with a 
        formal response.

        Args:
            user_input: The raw input received from the user.

        Returns:
            A formated string containing the formal response

        .. impl::
            :id: GET_RESPONSE
            :implements: REQ_08
        """
        split_message: list[str] = re.split(r'\s+|[?.,\';:-]\s*', user_input.lower())
        response:str = long.check_all_messages(split_message)
        parsed_response: str = self.response_parser(response)
        return parsed_response