import PySimpleGUI as sg
import time as t

sg.theme('DarkAmber')
pomodoro = 25
sec = pomodoro * 60
minn, secc = divmod(sec, 60)
time_format = '{:02d}:{:02d}'.format(minn, secc)


layout = [  [sg.Text('Pomodoro Timer')],
            [sg.Text(size=(10,1), font='Any 45', key='-OUT-')],
            [sg.Button('Start'), sg.Button('Pause'), sg.Button('Cancel')]]

window = sg.Window('Pomodoro Timer', layout)

running = False
while True:
  event, values = window.read(timeout=1000)
  if event == sg.WIN_CLOSED or event == 'Cancel':
    break
  if event == 'Start':
    sec = pomodoro * 60
    running = True
  if running:
    minn, secc = divmod(sec, 60)
    time_format = '{:02d}:{:02d}'.format(minn, secc)
    window['-OUT-'].update(time_format)
    sec -= 1
  if event == 'Pause':
    running = not running

window.close()