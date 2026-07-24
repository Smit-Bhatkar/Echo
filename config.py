# ==========================
# Audio Settings
# ==========================

SAMPLERATE = 16000
CHANNELS = 1
CHUNK_SIZE = 512

# ==========================
# Whisper Settings
# ==========================

WHISPER_MODEL = "base.en"
WHISPER_DEVICE = "cpu"
WHISPER_COMPUTE_TYPE = "int8"
BEAM_SIZE = 5
LANGUAGE = "en"

# ==========================
# Voice Activity Detection
# ==========================

VAD_THRESHOLD = 0.55
MIN_SILENCE_MS = 700
SPEECH_PAD_MS = 200
LISTEN_TIMEOUT = 10

# ==========================
# Pre-roll Buffer
# ==========================

PREROLL_MS = 500