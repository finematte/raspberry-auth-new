import os
import subprocess

DEVICE_ID_FILE_PATH = "/var/lib/greenmind/device_id.txt"


def save_device_id(device_id):
    directory = "/var/lib/greenmind"
    
    if not os.path.exists(directory):
        os.makedirs(directory, mode=0o700)
        
    subprocess(["sudo", "chmod", "7777", "/var/lib/greenmind"])
    
    try:
        with open(DEVICE_ID_FILE_PATH, "w") as file:
            file.write(str(device_id))
    except IOError as e:
        print(f"Error saving device ID: {e}")
