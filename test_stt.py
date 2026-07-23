from core.stt import STT

stt = STT()

while True:
    text = stt.listen()
    print("You said:", text)