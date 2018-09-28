try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import paramiko
from scp import SCPClient
import subprocess
import sox
import wave

import urllib.request

import urllib.parse

import requests
import json


WAVE_FILE_NAME = "test1.wav"

subprocess.call(["rec", "-c", "1", "-r", "16000", WAVE_FILE_NAME, "silence", "1", "0.1", "3%", "1", "3.0", "3%"])
print("Recording done..")
subprocess.call(["aplay", WAVE_FILE_NAME])


# Send file to ML-Comp: 
server = '192.168.229.121'
port = 22
user = 'scj'
seva_url = 'http://192.168.229.121:8000/seva'
remote_path = "/home/TAI/tai_brain/taiserver"
key_file_location = "/home/pi/.ssh/id_rsa"
with open(key_file_location, 'r') as keyfile:
   pk = paramiko.RSAKey.from_private_key(keyfile)
    
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=server,username=user,pkey=pk)

with SCPClient(ssh.get_transport()) as scp:
    scp.put(WAVE_FILE_NAME, remote_path) # Copy my_file.txt to the server
    
ssh.close()

r = requests.get(url = seva_url)

seva_ack = r.text
print(seva_ack)

