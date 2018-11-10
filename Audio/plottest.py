import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile
import wave
import sys

spf = wave.open('data/ch2.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')

print(len(signal))

#263000 - 285000 is the word man

for i in range(263000, 285000):
    signal[i] = 5000 * np.sin(2 * np.pi * 1000 / 44100 * i)

#510000 - 535000
for i in range(510000, 535000):
    signal[i] = 5000 * np.sin(2 * np.pi * 1000 / 44100 * i)

youtubeChannel = "youtube.com/pewdiepie"
lengthYoutube = len(youtubeChannel)
listC = list(youtubeChannel)
for i in range(len(listC)):
    listC[i] = ord(listC[i])

#encode youtube channel into file
for c in range(lengthYoutube):
    signal[c + 263000] = listC[c]

for c in range(lengthYoutube):
    signal[c + 510000] = listC[c] 

#scipy.io.wavfile.write('data/new.wav', 44100, signal)

#sys.exit(0)

#If Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal)

plt.show()

