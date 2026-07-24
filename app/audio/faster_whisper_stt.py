from faster_whisper import WhisperModel

from app.audio.speech_recognizer import SpeechRecognizer


class FasterWhisperSTT(SpeechRecognizer):

    def __init__(self):

        print("Loading Faster Whisper...")

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

        print("Speech Recognition Ready!")

    def transcribe(self, audio_path: str):

        segments, info = self.model.transcribe(
            audio_path,
            language="en",
            beam_size=5,
            vad_filter=True,
            vad_parameters=dict(
                min_silence_duration_ms=500
            )
        )

        print("\nDetected Language:", info.language)
        print("Probability:", info.language_probability)

        text = ""

        print("\nSegments:")

        for segment in segments:
            print(
                f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}"
            )

            text += segment.text

        return text.strip()