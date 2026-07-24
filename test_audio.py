from app.audio.microphone import Microphone
from app.audio.faster_whisper_stt import FasterWhisperSTT
from app.interfaces.voice_interface import VoiceInterface
from app.core.conversation_engine import ConversationEngine

engine = ConversationEngine()

voice = VoiceInterface(engine)

voice.listen()

mic = Microphone()

stt = FasterWhisperSTT()

audio = mic.record()

text = stt.transcribe(audio)

print("\nYou said:")

print(text)