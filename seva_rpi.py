import paramiko
from scp import SCPClient
import subprocess
import sox
import wave


WAVE_FILE_NAME = "test1.wav"

subprocess.call(["sox", "-t", "waveaudio", "-c", "1", "-r", "16000", "-d", WAVE_FILE_NAME, "silence", "1", "0.1", "3%", "1", "3.0", "3%"])
print("Recording done..")
subprocess.call(["aplay", WAVE_FILE_NAME])


# Send file to ML-Comp: 
server = '192.168.229.92'
port = 22 
user = 'mllaptop'
password = 'Semcon196' 

def createSSHClient(server, port, user, password):
	client = paramiko.SSHClient()
	client.load_system_host_keys()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(server, port, user, password)
	return client
	
ssh = createSSHClient(server, port, user, password)

with SCPClient(ssh.get_transport()) as scp:
	scp.put(WAVE_FILE_NAME, WAVE_FILE_NAME) # Copy my_file.txt to the server