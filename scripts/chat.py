#chat.py
import utilities.long_responses as long
import re
from scripts.solar_system import planets
from tabulate import tabulate
import scripts.response
import scripts.chat_history

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
        self.planet_instance = planets()
        self.user_input = ""
        self.bot_response = ""
        self.chat_history = scripts.chat_history.chat_history()

    def get_user_input(self) -> str:
        """Gets the user input from the console and sanitises it of special characters.

        :returns: The user input
        :rtype: str 

        .. impl::
            :id: CHT_GET_USER_INPUT
            :implements: REQ001
            :tests: TTC001
        """
        return self.user_input
    
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
        """Gets the processed response from the bot based on the user input, saving it to the bot_response attribute.

        :param str user_input: The raw input received from the user.

        .. impl::
            :id: CHT_GET_RESPONSE
            :implements: REQ001
            :tests: TTC001
        """
        response = scripts.response.response()
        self.bot_response = response.get_response(user_input)

    def display_bot_response(self) -> str:
        """Gets the processed response from the bot based on the user input, saving it to the bot_response attribute.

        .. impl::
            :id: GET_RESPONSE
            :implements: REQ001
            :tests: TTC001
        """
        return self.bot_response
    
    def record_chat(self) -> None:
        """Records the chat history by appending the user input and bot response to the chat history.

        .. impl::
            :id: CHT_RECORD_CHAT
            :implements: REQ001
            :tests: TTC001
        """
        self.chat_history.update_chat_history(dict({self.user_input, self.bot_response}))

    def clear_chat_history(self) -> None:
        """Clears the chat history.

        .. impl::
            :id: CHT_CLEAR_CHAT_HISTORY
            :implements: REQ001
            :tests: TTC001
        """
        self.chat_history.purge_chat()