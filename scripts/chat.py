#chat.py
import utilities.long_responses as long
import re
from scripts.solar_system import planets
from tabulate import tabulate

class chat:
    """Planetarium chatbot

    .. impl::
        :id: PLANITARIUM_CHATBOT
        :implements: REQ_01, REQ_02
    """
    def __init__(self) -> None:
        self.planet_instance = planets()

    

    
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
            :implements: REQ001
        """
        split_message: list[str] = re.split(r'\s+|[?.,\';:-]\s*', user_input.lower())
        response:str = long.check_all_messages(split_message)
        parsed_response: str = self.response_parser(response)
        return parsed_response