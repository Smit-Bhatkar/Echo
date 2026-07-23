import subprocess
import os
import tempfile
from playsound3 import playsound

class PiperTTS:

    def __init__(self):

        self.piper_path = os.path.join("piper", "piper.exe")

        self.model_path = os.path.join(
            "piper",
            "models",
            "en_US-lessac-medium.onnx"
        )

    def speak(self, text):

     temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
     )

     temp_file.close()

     subprocess.run(
         [
             self.piper_path,
             "-m",
             self.model_path,
             "-f",
             temp_file.name,
         ],
         input=text,
         text=True,
         check=True,
     )

     playsound(temp_file.name)

     os.remove(temp_file.name)