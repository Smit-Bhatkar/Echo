import os
import tempfile

import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel


class STT:

    def __init__(self):
        print("Loading Whisper model...")

        self.model = WhisperModel(
            "base.en",
            device="cpu",
            compute_type="int8"
        )

        self.samplerate = 16000
        self.channels = 1

        print("Whisper loaded successfully.")

    def _record_audio(self, duration=5):
        """Record audio from the microphone."""

        print("🎤 Listening...")

        recording = sd.rec(
            int(duration * self.samplerate),
            samplerate=self.samplerate,
            channels=self.channels,
            dtype="int16"
        )

        sd.wait()

        return recording

    def _save_audio(self, recording):
        """Save recording to a temporary WAV file."""

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_audio:

            write(
                temp_audio.name,
                self.samplerate,
                recording
            )

            return temp_audio.name

    def _transcribe_audio(self, audio_path):
        """Convert speech to text."""

        print("🧠 Transcribing...")

        segments, info = self.model.transcribe(
            audio_path,
            beam_size=5,
            language="en"
        )

        text = ""

        for segment in segments:
            text += segment.text

        os.remove(audio_path)

        return text.strip()

    def listen(self):
        """Main listening pipeline."""

        recording = self._record_audio()

        audio_path = self._save_audio(recording)

        return self._transcribe_audio(audio_path)