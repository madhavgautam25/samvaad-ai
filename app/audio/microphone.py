import sounddevice as sd
import soundfile as sf


class Microphone:

    SAMPLE_RATE = 16000

    def record(
        self,
        duration=5,
        output_file="temp.wav"
    ):

        print("\n🎤 Listening...")

        recording = sd.rec(
            int(duration * self.SAMPLE_RATE),
            samplerate=self.SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        sf.write(
            output_file,
            recording,
            self.SAMPLE_RATE
        )

        print("✅ Recording Finished")

        return output_file