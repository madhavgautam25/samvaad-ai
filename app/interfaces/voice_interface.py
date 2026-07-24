from app.audio.microphone import Microphone
from app.audio.faster_whisper_stt import FasterWhisperSTT


class VoiceInterface:

    def __init__(self, conversation_engine):

        self.engine = conversation_engine
        self.microphone = Microphone()
        self.stt = FasterWhisperSTT()

    def listen(self):

        audio = self.microphone.record()

        text = self.stt.transcribe(audio)

        if not text:
            print("Didn't catch that.")
            return None

        print(f"\nUser: {text}")

        response = self.engine.chat(text)

        print(f"\nSamvaad: {response}")

        return response