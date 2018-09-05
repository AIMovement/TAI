import subprocess

import sox
import wave


WAVE_FILE_NAME = "test1.wav"

subprocess.call(["rec", "-c", "1", "-r", "16000",WAVE_FILE_NAME, "silence", "1", "0.1", "3%", "1", "3.0", "3%"])
print("Recording done..")
subprocess.call(["aplay", WAVE_FILE_NAME])

