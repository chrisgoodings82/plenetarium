#chat.py
from scripts.solar_system import solar_system
import scripts.response

class chat:

    _instance = None
    
    def __new__(cls):
        """Creates a singleton instance of the chat class
        
        :return: An instance of the class.
        :rtype: chat
        """
        if cls._instance is None:
            cls._instance = super(chat, cls).__new__(cls)
            cls._instance.init_chat()
        return cls._instance

    def init_chat(self) -> None:
        """Initialises the chat instance with necessary attributes."""
        self.planet_instance = solar_system()
        self.user_input = ""
        self.bot_response = ""

    def get_user_input(self) -> str:
        """Gets the user input from the console and sanitises it of special characters.

        :returns: The user input
        :rtype: str 

        .. impl::
            :id: CHT_GET_USER_INPUT
            :implements: REQ001
            :tests: TTC001
        """
        return str(self.user_input)
    
    def get_bot_response(self) -> str:
        """Gets the bot response.

        :returns: The bot response
        :rtype: str 

        .. impl::
            :id: CHT_GET_BOT_RESPONSE
            :implements: REQ001
            :tests: TTC001
        """
        return self.bot_response

    def get_response(self, user_input: str) -> None:
        """Creates an instance of the response class, passes in the user's query to receive an appropriate response

        :param str user_input: The raw input received from the user.

        .. impl::
            :id: CHT_GET_RESPONSE
            :implements: REQ001
            :tests: TTC001
        """
        self.bot_response = scripts.response.get_response(user_input)

    def display_bot_response(self) -> str:
        """Gets the processed response from the bot based on the user input, saving it to the bot_response attribute.

        .. impl::
            :id: CHAT_GET_RESPONSE
            :implements: REQ001
            :tests: TTC001
        """
        return self.bot_response