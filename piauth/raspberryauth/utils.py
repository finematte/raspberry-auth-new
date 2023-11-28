DEVICE_ID_FILE_PATH = "C:/Users/1337/Desktop/device_id.txt"


def save_device_id(device_id):
    try:
        with open(DEVICE_ID_FILE_PATH, "w") as file:
            file.write(device_id)
    except IOError as e:
        print(f"Error saving device ID: {e}")
