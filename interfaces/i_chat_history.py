# i_chat_history.py
from abc import ABC, abstractmethod
from queue import Queue

class i_chat_history(ABC):
    """An interface for the chat history."""

    @abstractmethod
    def get_chat_history() -> Queue[dict[str, str]]:
        """Gets the chat history as a queue."""
        pass

    @abstractmethod
    def update_chat_history(chat_exchange: dict[str, str]) -> bool:
        """Adds a new chat history item to the queue."""
        pass

    @abstractmethod
    def purge_chat() -> None:
        """Clears the entire chat history."""
        pass

    @abstractmethod
    def get_chat_history_limit() -> int:
        """Gets the size of the chat history queue."""
        pass

    @abstractmethod
    def set_chat_history_limit(linit: int) -> None:
        """Allows the size of the chat history to be changed."""
        pass