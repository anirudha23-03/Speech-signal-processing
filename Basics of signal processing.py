import wave
import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import math
import matplotlib.pyplot as plt
import librosa
from pydub import AudioSegment
#%matplotlib inline

#load data
wav_obj = wave.open('Impact moderato.wav', 'rb')
channels = wav_obj.getnchannels() # get number of channels
sam_wid = wav_obj.getsampwidth()  # width of the sample 
f_rate = wav_obj.getframerate()   # sampling frequency
no_f = wav_obj.getnframes()       # the number of individual frame
para = wav_obj.getparams()        # to get the parameters of wave 
t_audio = no_f/f_rate             # length of audio in seconds

#print the values
print(channels)
print(sam_wid)
print(f_rate)
print(no_f)
print(para)
print(t_audio)

# the amplitude of the wave at that point in time
signal_wave = wav_obj.readframes(no_f)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print("The signal array is",signal_array)

#To split the data into individual channels, we can use a clever little array slice trick:
l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

#plotting the signal amplitude left channel
times = np.linspace(0, t_audio, num=no_f)
plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Left Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()

#plotting the signal amplitude right channel
times = np.linspace(0, t_audio, num=no_f)
plt.figure(figsize=(15, 5))
plt.plot(times, r_channel)
plt.title('Right Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()

#analysing the frequency spectrum of left channel
plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=f_rate, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()

#analysing the frequency spectrum of left channel
plt.figure(figsize=(15, 5))
plt.specgram(r_channel, Fs=f_rate, vmin=-20, vmax=50)
plt.title('Right Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()
