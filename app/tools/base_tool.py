from abc import ABC, abstractmethod


class BaseTool(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def can_handle(self, message: str):
        pass

    @abstractmethod
    def execute(self, message: str):
        pass