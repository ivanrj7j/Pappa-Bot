import pyautogui as pag
import json
import PySimpleGUI as psg
import requests

file = open('setting.json', )
setting_file = json.load(file)
setting = setting_file['settings']
default = setting_file['default']
total_KM = setting_file['total_KM']
file.close()

api = 'AIzaSyAsCWEr8qrSLKn2V3FhJDvCad_KkR5OltY'


layout = [[psg.Text("Nammuku Thudanghiyalo?")],
          [psg.Text('From', size=(15, 1), key='from'), psg.InputText()],
          [psg.Text('To', size=(15, 1), key='to'), psg.InputText()],
          [psg.Submit()]]
window = psg.Window(title="Appa Bot", layout=layout)


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == psg.WIN_CLOSED:
        break
    if event == "Submit":
        print(f"from: {values[0]} and to: {values[1]}")
        url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
        u = url + 'origins=' + values[0] +'&destinations=' + values[1] +'&key=' + 'AIzaSyAsCWEr8qrSLKn2V3FhJDvCad_KkR5OltY'
        print(u)
        r = requests.get(u)
        distance = r.json()
        print(distance)
        e, v = psg.popup("Distance", "55", 'Money', str(55*4.25))
    if e and e == 'O':
        print('meow')
window.close()
