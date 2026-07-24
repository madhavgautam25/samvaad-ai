from abc import ABC, abstractmethod


class SpeechRecognizer(ABC):

    @abstractmethod
    def transcribe(self, audio_path: str) -> str:
        pass