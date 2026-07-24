import os
import tempfile
import config
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
             config.WHISPER_MODEL,
             device=config.WHISPER_DEVICE,
             compute_type=config.WHISPER_COMPUTE_TYPE
        )

        self.samplerate = config.SAMPLERATE
        self.channels = config.CHANNELS
        self.chunk_size = config.CHUNK_SIZE


        # ---------- Silero VAD ----------

        

        self.vad_model = load_silero_vad()

        self.vad_iterator = VADIterator(
             self.vad_model,
             sampling_rate=self.samplerate,
             threshold=config.VAD_THRESHOLD,
             min_silence_duration_ms=config.MIN_SILENCE_MS,
             speech_pad_ms=config.SPEECH_PAD_MS
        )

        print("Whisper loaded successfully.")

    def _record_audio(self):
        """Record audio until Silero detects speech has ended."""

        print("🎤 Listening...")

        # Reset VAD state for a fresh recording
        self.vad_iterator.reset_states()

        audio_queue = queue.Queue()
        recorded_chunks = []

        recording_started = False

        LISTEN_TIMEOUT = config.LISTEN_TIMEOUT

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

             start_time = time.time()

             while True:

                   # No speech for too long
                   if not recording_started and time.time() - start_time > LISTEN_TIMEOUT:
                      print("❌ No speech detected.")
                      return np.zeros((1, 1), dtype=np.int16)

                   chunk = audio_queue.get()

                   # Save original chunk
                   audio_chunk = chunk.copy()
 
                   # Prepare for Silero
                   vad_chunk = torch.from_numpy(chunk.squeeze())

                   event = self.vad_iterator(vad_chunk)

                   # Speech started
                   if event and "start" in event:
                     print("🟢 Speech detected")
                     recording_started = True

                   # Save only after speech starts
                   if recording_started:
                     recorded_chunks.append(audio_chunk)

                   # Speech ended
                   if event and "end" in event:
                      print("🔴 Speech ended")
                      break

        if not recorded_chunks:
           return np.zeros((1, 1), dtype=np.int16)

        recording = np.concatenate(recorded_chunks, axis=0)

        recording = (recording * 32767).astype(np.int16)

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
            beam_size=config.BEAM_SIZE,
            language=config.LANGUAGE
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