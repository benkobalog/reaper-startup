import PySimpleGUI as sg                     
import os

layout = [  [sg.Button("Focusrite"), sg.Button("Asio") ],  
            [sg.Button('Focusrite + Nektar'), sg.Button("Asio + Nektar")],
            [sg.Button('Focusrite + Mini'), sg.Button("Asio + Mini")],
            [sg.Button('Focusrite + Microlab'), sg.Button("Asio + Microlab")] 
            ]

window = sg.Window('Reaper Launcher', layout)

event, values = window.read()

options = event.split(" + ")
driverStr = options[0]
midiStr = options[1] if len(options) == 2 else "no midi"

print(event, values, driverStr, midiStr)

drivers = {
    "Asio":  ("0", "ASIO4ALL v2"),
    "Focusrite": ("1", "Focusrite USB ASIO")
}
midis = {
    "no midi" : "0",
    "Nektar" : "2",
    "Mini" : "8",
    "Microlab" : "16"
}

driver = drivers[driverStr]
midi = midis[midiStr]
print("Setting config to: driver=" + str(driver) + ", midi=" + str(midi))

userName = os.getlogin()
reaperConfig = f"C:\\Users\\{userName}\\AppData\\Roaming\\REAPER\\REAPER.ini"

def rewriteLine(line):
    if(line.startswith("asio_driver=")):
        return f'asio_driver="{driver[0]}"'
    elif(line.startswith("asio_driver_name=")):
        return f'asio_driver_name="{driver[1]}"'
    elif(line.startswith("midiins=")):
        return f'midiins={midi}'
    elif(line.startswith("midiins_cs=")):
        return f'midiins_cs={midi}'
    else:
        return line

with open(reaperConfig) as file:
    allLines = [line.rstrip('\n') for line in file]
    updatedLines = list(map(rewriteLine, allLines))

with open(reaperConfig, "w") as file:
    file.write("\n".join(updatedLines))

window.close()

import subprocess
subprocess.Popen(["C:\\Program Files\\REAPER (x64)\\reaper.exe"])
