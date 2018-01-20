from matplotlib.mlab import find
import pyaudio
import numpy as np
import math

chunk = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20


def Pitch(signal):
    signal = np.fromstring(signal, 'Int16');
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing));
    f0=round(len(index) *RATE /(2*np.prod(len(signal))))
    return f0;


p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
channels = CHANNELS,
rate = RATE,
input = True,
output = True,
frames_per_buffer = chunk)

def getFrequency():
    frequencies= []
    for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
        data = stream.read(chunk)
        Frequency=Pitch(data)
        frequencies.append(Frequency)
    desiredFrequency=max(frequencies)-min(frequencies)
    return desiredFrequency
    
def getNote():
    num= getFrequency()
    if num>2900 and num<3000:
        pyautogui.press('up')
        print("b")
    if num == 2627 or num == 2606 or num == 2649 or num == 2584:
    	pyautogui.press('down')
    	print("a")
    if num == 2326 or num == 2304 or num == 2347 or num == 2369:
    	pyautogui.press('left')
    	print("g")
    elif num ==581 or num == 560 or num == 603:
        pyautogui.press('right')
    	print("Low D")
    else:
    	print ("Frequency: ",Frequency)

getNote()
