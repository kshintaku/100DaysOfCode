'''
Day 8 Project

Description:
Using PySimpleGUI to make a Pomodoro Timer

Requirements:
Needs 'mpg123' to be installed in os
Ex. 'brew install mpg123'

TODO:
base on internal time to prevent drift and other timing issues
resolve issue of timer ending and skipping 1 second while playing sound

CREDIT:
Audio thanks to SoundBible.com
'''

import PySimpleGUI as sg
import os
import time as t

sg.theme('DarkAmber')
pomodoro = 1
sec = pomodoro * 60
minn, secc = divmod(sec, 60)
time_format = '{:02d}:{:02d}'.format(minn, secc)
start_btn = "Start"


layout = [  [sg.Text('Pomodoro Timer', font='Any 15')],
            [sg.Text(text=time_format, size=(10,1), font='Any 45', key='-OUT-')],
            [ sg.Button('Start', image_filename="start.png", font='Any 20', disabled=False, key='btn1'), 
              sg.Button('Pause', image_filename="pause.png", font='Any 20', key='btn2', disabled=True), 
              sg.Button('Reset', image_filename="reset.png", font='Any 20', disabled=True, key='btn3')]]

window = sg.Window('Pomodoro Timer', layout)

running = False
while True:
  event, values = window.read(timeout=1000)
  if event == sg.WIN_CLOSED or event == 'Cancel':
    break
  if event == 'Start' or event == 'btn1':
    window['btn1'].update(disabled=True)
    window['btn3'].update(disabled=False)
    if time_format == '00:00':
      running = False
    else:
      running = True
  if running:
    minn, secc = divmod(sec, 60)
    time_format = '{:02d}:{:02d}'.format(minn, secc)
    window['-OUT-'].update(time_format)
    window['btn2'].update(disabled=False)
    sec -= 1
  if event == 'Pause' or event == 'btn2':
    running = False
    window['btn1'].update(disabled=False)
  if event == 'Reset' or event == 'btn3':
    running = False
    sec = pomodoro * 60
    minn, secc = divmod(sec, 60)
    time_format = '{:02d}:{:02d}'.format(minn, secc)
    window['-OUT-'].update(time_format)
    window['btn1'].update(disabled=False)
    window['btn3'].update(disabled=True)
  if not running:
    window['btn2'].update(disabled=True)
  if time_format == '00:01':
    os.system('mpg123 alert-bell.mp3')
    time_format = '00:00'
    window['-OUT-'].update(time_format)
    running = False

window.close()
