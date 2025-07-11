# chat_history.py
from queue import Queue
from interfaces.i_chat_history import i_chat_history

class chat_history(i_chat_history):
    """The concrete class for the i_chat_history interface."""

    _instance = None
    
    def __new__(cls):
        """Creates a singleton instance of the chat_history class
        
        :return: An instance of the class.
        :rtype: chat_history
        """
        if cls._instance is None:
            cls._instance = super(chat_history, cls).__new__(cls)
            cls._instance.init_chat_history()
        return cls._instance
        
    def init_chat_history(self):
        """Initialises the Chat History log and sets the initial size to 10 entries.

        .. impl::
            :implements: REQ001
            :tests: TTC001
        """
        self.chat_history_limit = 10
        self.chat_history = Queue(maxsize=self.chat_history_limit)

    def get_chat_history(self) -> Queue[dict[str, str]]:
        """Gets the chat history as a queue.

        :return: The contents of the Chat History log.
        :rtype: Queue[dict[str, str]].

        .. impl::
            :implements: REQ001
            :tests: TTC001
        """
        return self.chat_history

    def update_chat_history(self, chat_exchange: dict[str, str]) -> None:
        """Adds a new chat history item to the queue.
        
        :param dict[str, str] chat_exchange: The chat exchange message to be stored.

        .. impl::
            :implements: REQ001
            :tests: TTC001
        """
        if self.chat_history.full():
            self.chat_history.get_nowait()
        self.chat_history.put_nowait(chat_exchange)

    def purge_chat(self) -> None:
        """Clears the entire chat history.

        .. impl::
            :implements: REQ001
            :tests: TTC001
        """
        while not self.chat_history.empty():
            self.chat_history.get_nowait()

    def get_chat_history_limit(self) -> int:
        """Gets the size of the chat history queue.

        :return: The size of the chat history.
        :rtype: int.

        .. impl::
            :implements: REQ001
            :tests: TTC001
        """
        return self.chat_history_limit

    def set_chat_history_limit(self, limit: int) -> None:
        """Allows the size of the chat history to be changed.
        
        :param int limit: The length of the chat history to be retained

        .. impl::
            :implements: REQ001
            :tests: TTC001
        """
        if limit < self.chat_history_limit:
            while range(0, self.chat_history_limit - limit):
                self.chat_history.get_nowait()
            self.chat_history_limit = limit
            self.chat_history.maxsize = self.chat_history_limit