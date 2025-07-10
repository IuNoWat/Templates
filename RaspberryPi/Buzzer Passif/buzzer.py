

import time
import os

import pigpio

#CONSTANTS
os.system("sudo pigpoid")
PIN=18
PI=pigpio.pi()
DEFAULT_OCTAVE=6
DEFAULT_DUTY = 50000

#INIT
PI.set_mode(PIN,pigpio.OUTPUT)

#NOTES
notes={
"C":[16,32,65,130,261,523,1046,2093,4186,],
"C#":[17,34,69,138,277,554,1108,2217,4434,],
"D":[18,36,73,146,293,587,1174,2349,4698,],
"D#":[19,38,77,155,311,622,1244,2489,4978,],
"E":[20,41,82,164,329,659,1318,2637,5274,],
"F":[21,43,87,174,349,698,1396,2793,5587,],
"F#":[23,46,92,185,369,739,1479,2959,5919,],
"G":[24,49,98,196,392,783,1567,3135,6271,],
"G#":[25,51,103,207,415,830,1661,3322,6644,],
"A":[27,55,110,220,440,880,1760,3520,7040,],
"A#":[29,58,116,233,466,932,1864,3729,7458],
"B":[30,61,123,246,493,987,1975,3951,7902],
" ":[0]
}

#CLASS

class Music() :
    def __init__(self,interval=0.1) :
        self.interval=interval

time_note=0.1



def play_note(note,duree,oct=DEFAULT_OCTAVE,duty=DEFAULT_DUTY) :
    PI.hardware_PWM(PIN,notes[note][oct],duty)
    time.sleep(duree)
    PI.hardware_PWM(PIN,0,duty)

def play_music(music) :
    for i,note in enumerate(music) :
        play_note(note["note"],note["time"],note["oct"])


play_music(zelda)

def play_all_notes(interval) :
    for i in range(0,9) :
        for key in notes :
            print(f"Playing note {key} at octave {i} : {notes[key][i]}")
            PI.hardware_PWM(PIN,notes[key][i],500000)
            time.sleep(interval)
    PI.hardware_PWM(PIN,0,500000)


#play_all_notes(0.1)

