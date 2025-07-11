# i_reader.py
from abc import ABC, abstractmethod

class i_reader(ABC):
    """An interface for JSON file reader implementation."""

    @abstractmethod
    def read(self, filename: str) -> dict:
        pass
