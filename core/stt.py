import os
import tempfile

import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import torch
import queue
import time
import numpy as np

from silero_vad import (
    load_silero_vad,
    VADIterator
)


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
        # ---------- Silero VAD ----------

        self.chunk_size = 512

        self.vad_model = load_silero_vad()

        self.vad_iterator = VADIterator(
             self.vad_model,
             sampling_rate=self.samplerate
        )

        print("Whisper loaded successfully.")

    def _record_audio(self):
        """Record audio using a streaming microphone."""

        print("🎤 Listening...")

        audio_queue = queue.Queue()
        chunks = []

        def callback(indata, frames, time_info, status):
            if status:
                print(status)

            audio_queue.put(indata.copy())

        with sd.InputStream(
             samplerate=self.samplerate,
             channels=self.channels,
             dtype="float32",
             blocksize=self.chunk_size,
             callback=callback,
        ):

             start = time.time()

             while time.time() - start < 5:
                   chunk = audio_queue.get()
                   chunks.append(chunk)

        recording = np.concatenate(chunks, axis=0)

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