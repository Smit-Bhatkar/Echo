import sounddevice as sd

SAMPLERATE = 16000
CHUNK_SIZE = 512


def callback(indata, frames, time, status):
    if status:
        print(status)

    print(f"Received chunk: {indata.shape}")


print("🎤 Speak into the microphone...")

with sd.InputStream(
    samplerate=SAMPLERATE,
    channels=1,
    dtype="float32",
    blocksize=CHUNK_SIZE,
    callback=callback,
):
    input("Press ENTER to stop...\n")