#chat.py
import utilities.long_responses as long
import re
from scripts.solar_system import solar_system
from tabulate import tabulate
from scripts.chat_history import chat_history

class chat:
    """Planetarium chatbot

    .. impl::
        :id: PLANITARIUM_CHATBOT
        :implements: REQ_01, REQ_02
    """
    _instance = None
    
    def __new__(cls):
        """Creates a singleton instance of the chat_history class
        
        :return: An instance of the class.
        :rtype: chat
        """
        if cls._instance is None:
            cls._instance = super(chat, cls).__new__(cls)
            cls._instance.init_chat()
        return cls._instance
    
    def init_chat(self):
        """Initialises the chat instance and sets up the response parser.

        .. impl::
            :id: CHAT_INIT_CHAT
            :implements: REQ001
            :tests: TTC001
        """
        self.chat_history = chat_history()
        self.solar_system = solar_system()

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