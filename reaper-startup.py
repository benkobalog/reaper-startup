import sys
import os

drivers = {
    "asio":  ("0", "ASIO4ALL v2"),
    "focusrite": ("1", "Focusrite USB ASIO")
}

selector = sys.argv[1]
driver = drivers[selector]
print("Setting config to " + str(driver))

userName = os.getlogin()
reaperConfig = f"C:\\Users\\{userName}\\AppData\\Roaming\\REAPER\\REAPER.ini"

def rewriteLine(line):
    if(line.startswith("asio_driver=")):
        return f'asio_driver="{driver[0]}"'
    elif(line.startswith("asio_driver_name=")):
        return f'asio_driver_name="{driver[1]}"'
    else:
        return line

with open(reaperConfig) as file:
    allLines = [line.rstrip('\n') for line in file]
    updatedLines = list(map(rewriteLine, allLines))

with open(reaperConfig, "w") as file:
    file.write("\n".join(updatedLines))

import subprocess
subprocess.Popen(["C:\\Program Files\\REAPER (x64)\\reaper.exe"])
