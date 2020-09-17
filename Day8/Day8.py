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

sg.theme('DarkBrown4')
pomodoro = 25
sec = pomodoro * 60
minn, secc = divmod(sec, 60)
time_format = '{:02d}:{:02d}'.format(minn, secc)
start_btn = "Start"


layout = [  [ sg.Text(
                text='Pomodoro Timer',
                font='Any 15',
                justification='center')],
            [ sg.Text(
                text=time_format,
                size=(6,1),
                font='Any 45',
                key='-OUT-',
                justification='center')],
            [ sg.Button(
                button_text='Start',
                font='Any 20',
                disabled=False,
                key='btn1',
                size=(6,1)), 
              sg.Button(
                button_text='Reset',
                font='Any 20',
                disabled=True,
                key='btn2',
                size=(6,1))]]

window = sg.Window('Pomodoro Timer', layout)

running = False
while True:
  event, values = window.read(timeout=1000)
  if event == sg.WIN_CLOSED or event == 'Cancel':
    break
  if event == 'btn1':
    if running:
      running = False
      window['btn1'].update('Start')
    else:
      running = True
      window['btn1'].update('Pause')
    window['btn2'].update(disabled=False)
    if time_format == '00:00':
      running = False
  if running == True:
    minn, secc = divmod(sec, 60)
    time_format = '{:02d}:{:02d}'.format(minn, secc)
    window['-OUT-'].update(time_format)
    window['btn2'].update(disabled=False)
    sec -= 1
  if event == 'btn2':
    running = False
    sec = pomodoro * 60
    minn, secc = divmod(sec, 60)
    time_format = '{:02d}:{:02d}'.format(minn, secc)
    window['-OUT-'].update(time_format)
    window['btn1'].update('Start')
    window['btn2'].update(disabled=True)
  if time_format == '00:01':
    os.system('mpg123 alert-bell.mp3')
    time_format = '00:00'
    window['-OUT-'].update(time_format)
    running = False

window.close()
